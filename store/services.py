from store.models import Price, Product, Store, Category
from rest_framework.response import Response
from rest_framework import status
from .utils import get_time


def build_obj_list(queryset):
    obj_list = []
    for product in queryset:
        product_obj = {
            "id": product.id,
            "name": product.name,
            "store": product.store_id.name,
            "category": product.category_id.name,
            "brand": product.brand,
            "size": product.size,
            "image": product.image_url,
            "redirect_page": product.page_url,
            "price": Price.objects.filter(product_id=product).last().price,
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
        "brand": product.brand,
        "size": product.size,
        "image": product.image_url,
        "redirect_page": product.page_url,
        "price": Price.objects.filter(product_id=product).last().price,
        "is_promotion": product.is_promotion,
    }
    return product_obj


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

    for product in products_list:
        try:
            category = Category.objects.get(name=product["category"].title())
        except Exception:
            return Response({"message": "Error in Category", "product": product}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product_obj = Product.objects.get(sku=product["sku"])
        except Product.DoesNotExist:
            product_obj = Product.objects.create(
                name=product["name"],
                store_id=store,
                category_id=category,
                sku=product["sku"],
                brand=product["brand"],
                size=product["size"],
                image_url=product["image_url"],
                page_url=product["page_url"],
                is_promotion=product["is_promotion"],
            )
        time_now = get_time()
        Price.objects.create(price=product["price"], date=time_now, product_id=product_obj)
    response = {"message": "Information Received"}
    return Response(response)
