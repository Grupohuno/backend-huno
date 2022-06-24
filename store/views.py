from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Category, Product

from .serializers import DummySerializer, ProductResponseSerializer
from .services import build_obj, build_obj_list, validate_and_save_data


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


class ProductsView(APIView, PageNumberPagination):
    page_size = 40

    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by("id")
        results = self.paginate_queryset(products, request, view=self)
        products_list = build_obj_list(results)
        serializer = ProductResponseSerializer(products_list, many=True)
        return self.get_paginated_response(serializer.data)


class CategoryView(APIView, PageNumberPagination):
    page_size = 40

    def get_category(self, category):
        try:
            return Category.objects.get(name=category)
        except Category.DoesNotExist:
            raise Http404 from None

    def get(self, request, category, *args, **kwargs):
        category_obj = self.get_category(category.title())
        products = Product.objects.filter(category_id=category_obj).order_by("id")
        results = self.paginate_queryset(products, request, view=self)
        products_list = build_obj_list(results)
        serializer = ProductResponseSerializer(products_list, many=True)
        return self.get_paginated_response(serializer.data)


class ProductView(APIView):
    def get_product(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404 from None

    def get(self, request, product_id, *args, **kwargs):
        product = self.get_product(product_id)
        related_products = Product.objects.filter(
            category_id=product.category_id
        ).exclude(id=product.id)
        recommended_products = sorted(related_products, key=lambda p: p.price())[:5]
        product_obj = build_obj(product)
        product_obj["recommended_products"] = build_obj_list(recommended_products)
        serializer = ProductResponseSerializer(product_obj)
        return Response(serializer.data)


class UpdateProductsView(APIView):
    def post(self, request, *args, **kwargs):
        response = validate_and_save_data(request)
        return response


class FilterProductsView(APIView, PageNumberPagination):
    page_size = 40

    def get_by_keyword(self, keyword, *args, **kwargs):
        products = Product.objects.all()
        try:
            return products.filter(name__icontains=keyword)
        except Product.DoesNotExist:
            raise Http404 from None

    def get_by_category(self, category, *args, **kwargs):
        products = Product.objects.all()
        try:
            return products.filter(category_id__name=category)
        except Product.DoesNotExist:
            raise Http404 from None

    def get(self, request, *args, **kwargs):
        keyword = request.query_params.get("keyword")
        filtered_products = self.get_by_keyword(keyword)
        products_by_category = self.get_by_category(keyword)
        set_keyword = set(filtered_products)
        set_category = set(products_by_category)
        set_final = set_keyword.union(set_category)
        if len(set_final) > 0:

            results = self.paginate_queryset(list(set_final), request, view=self)
            products_list = build_obj_list(results)
            serializer = ProductResponseSerializer(products_list, many=True)
            return self.get_paginated_response(serializer.data)
        raise Http404 from None

class NonPaginateProductsView(APIView):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by("id")
        products_list = build_obj_list(products)
        serializer = ProductResponseSerializer(products_list, many=True)
        return Response(serializer.data)

class NonPaginateFilterProductsView(APIView):

    def get_by_keyword(self, keyword, *args, **kwargs):
        products = Product.objects.all()
        try:
            return products.filter(name__icontains=keyword)
        except Product.DoesNotExist:
            raise Http404 from None

    def get_by_category(self, category, *args, **kwargs):
        products = Product.objects.all()
        try:
            return products.filter(category_id__name=category)
        except Product.DoesNotExist:
            raise Http404 from None

    def get(self, request, *args, **kwargs):
        keyword = request.query_params.get("keyword")
        filtered_products = self.get_by_keyword(keyword)
        products_by_category = self.get_by_category(keyword)
        set_keyword = set(filtered_products)
        set_category = set(products_by_category)
        set_final = set_keyword.union(set_category)
        if len(set_final) > 0:
            products_list = build_obj_list(list(set_final))
            serializer = ProductResponseSerializer(products_list, many=True)
            return Response(serializer.data)
        raise Http404 from None