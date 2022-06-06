# Create your views here.

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Category, Price, Product, Store

# import api.store.serializers as serializers
from .serializers import DummySerializer, ProductResponseSerializer
from .utils import get_time
from .services import build_obj_list, build_obj, validate_and_save_data


class DummyView(APIView):
    def get(self, request, *args, **kwargs):
        obj = {
            "message": "Dummy success",
        }
        serializer = DummySerializer(data=obj)
        if serializer.is_valid():
            print("Valido el Serialiers")
            return Response(obj)
        return Response({})


class ProductsView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by("id")
        products_list = build_obj_list(products)
        serializer = ProductResponseSerializer(products_list, many=True)
        return Response(serializer.data)


class CategoryView(APIView):
    def get_category(self, category):
        try:
            return Category.objects.get(name=category)
        except Category.DoesNotExist:
            raise Http404 from None

    def get(self, request, category, *args, **kwargs):
        category_obj = self.get_category(category.title())
        products = Product.objects.filter(category_id=category_obj).order_by("id")
        products_list = build_obj_list(products)
        serializer = ProductResponseSerializer(products_list, many=True)
        return Response(serializer.data)


class ProductView(APIView):
    def get_product(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404 from None

    def get(self, request, product_id, *args, **kwargs):
        product = self.get_product(product_id)
        product_obj = build_obj(product)
        serializer = ProductResponseSerializer(product_obj)
        return Response(serializer.data)


class UpdateProductsView(APIView):
    def post(self, request, *args, **kwargs):
        response = validate_and_save_data(request)
        return response


class FilterProductsView(APIView):
    def get_by_keyword(self, keyword, *args, **kwargs):
        products = Product.objects.all()
        try:
            return products.filter(name__icontains=keyword)
        except Product.DoesNotExist:
            raise Http404 from None

    def get(self, request, *args, **kwargs):
        response = []
        print(request.query_params)
        keyword = request.query_params.get("keyword")
        filtered_products = self.get_by_keyword(keyword)
        print(filtered_products)
        if len(filtered_products) > 0:
            for product in filtered_products:
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
                response.append(product_obj)
            return Response(response)
        raise Http404 from None
