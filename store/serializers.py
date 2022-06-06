from rest_framework import serializers
from store.models import Store, Product, Category


class DummySerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)


class StoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductResponseSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name =  serializers.CharField(max_length=180)
    store= serializers.CharField(max_length=180)
    category= serializers.CharField(max_length=180)
    brand=serializers.CharField(max_length=180)
    size=serializers.CharField(max_length=180)
    image=serializers.CharField(max_length=280)
    redirect_page=serializers.CharField(max_length=280)
    price=serializers.IntegerField()
    is_promotion=serializers.BooleanField()

