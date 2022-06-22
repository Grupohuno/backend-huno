from rest_framework import serializers


class DummySerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)


class ProductResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=180)
    store = serializers.CharField(max_length=180)
    category = serializers.CharField(max_length=180)
    sku = serializers.CharField(max_length=180)
    brand = serializers.CharField(max_length=180)
    size = serializers.CharField(max_length=180)
    image = serializers.CharField(max_length=280)
    redirect_page = serializers.CharField(max_length=280)
    price = serializers.IntegerField()
    is_promotion = serializers.BooleanField()
    recommended_products = serializers.ListField(default=None)


class ProductPostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=180)
    store = serializers.CharField(max_length=180, required=False)
    category = serializers.CharField(max_length=180)
    sku = serializers.CharField(max_length=180)
    brand = serializers.CharField(max_length=180)
    size = serializers.CharField(max_length=180)
    image_url = serializers.CharField(max_length=280)
    page_url = serializers.CharField(max_length=280)
    price = serializers.IntegerField()
    is_promotion = serializers.BooleanField(default=False)
