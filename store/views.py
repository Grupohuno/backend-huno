# Create your views here.
from math import prod
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Category, Price, Product

# import api.store.serializers as serializers
from .serializers import DummySerializer


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
        response = []
        products = Product.objects.all()
        for product in products:
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
            }
            response.append(product_obj)
        return Response(response)


class CategoryView(APIView):
    def get_category(self, category):
        try:
            return Category.objects.get(name=category)
        except Category.DoesNotExist:
            raise Http404 from None

    def get(self, request, category, *args, **kwargs):
        category_obj = self.get_category(category.title())
        response = []
        products = Product.objects.filter(category_id=category_obj)
        for product in products:
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
            }
            response.append(product_obj)
        return Response(response)

class ProductView(APIView):
    def get_product(self, product_id):
        print(product_id)
        print(type(product_id))
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404 from None

    def get(self, request, product_id, *args, **kwargs):
        product= self.get_product(product_id)
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
            }
        return Response(product_obj)

class UpdateProductsView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            print(request.data)
            response={"message": "Information Received"}
            return Response(response)
        except:
            response={"message": "ERROR"}
            return Response(response)