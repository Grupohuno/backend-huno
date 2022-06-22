from rest_framework import status
from rest_framework.response import Response

from store.models import Category, Price, Product, Store

from .serializers import ProductPostSerializer
from .utils import get_time


def build_obj_list(queryset):
    obj_list = []
    for product in queryset:
        product_obj = {
            "id": product.id,
            "name": product.name,
            "store": product.store_id.name,
            "category": product.category_id.name,
            "sku": product.sku,
            "brand": product.brand,
            "size": product.size,
            "image": product.image_url,
            "redirect_page": product.page_url,
            "price": product.price(),
            "is_promotion": product.is_promotion,
        }
        obj_list.append(product_obj)
    return obj_list


def build_obj(product):
    product_obj = {
        "id": product.id,
        "name": product.name,
        "store": product.store_id.name,
        "category": product.category_id.name,
        "sku": product.sku,
        "brand": product.brand,
        "size": product.size,
        "image": product.image_url,
        "redirect_page": product.page_url,
        "price": product.price(),
        "is_promotion": product.is_promotion,
    }
    return product_obj


def validate_price(product, price):
    old_price = Price.objects.filter(product_id=product).last()
    
    if old_price:
        variation = abs(old_price.price - price) * 100 / old_price.price
        return (variation < 200 and price > 0)
    
    return True


def validate_and_save_data(request):
    try:
        store_name = request.data["store"].title()
        products_list = request.data["products_list"]
    except Exception:
        return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        store = Store.objects.get(name=store_name)
    except Exception:
        return Response({"message": "Invalid store"}, status=status.HTTP_400_BAD_REQUEST)

    error_list_products = []
    for product in products_list:
        serializer = ProductPostSerializer(data=product)
        if serializer.is_valid():
            try:
                category = Category.objects.get(name=product["category"].title())
            except Exception:
                return Response(
                    {"message": "Error in Category", "product": product}, status=status.HTTP_400_BAD_REQUEST
                )
            try:
                product_obj = Product.objects.get(sku=product["sku"])
            except Product.DoesNotExist:
                product_obj = Product.objects.create(
                    name=serializer.data["name"],
                    store_id=store,
                    category_id=category,
                    sku=serializer.data["sku"],
                    brand=serializer.data["brand"],
                    size=serializer.data["size"],
                    image_url=serializer.data["image_url"],
                    page_url=serializer.data["page_url"],
                    is_promotion=serializer.data["is_promotion"],
                )
            time_now = get_time()
            if validate_price(product_obj, product["price"]):
                Price.objects.create(price=product["price"], date=time_now, product_id=product_obj)
        else:
            print(serializer.errors)
            error_list_products.append(product)

    response = {"message": "Information Received", "error_products": error_list_products}
    return Response(response)
