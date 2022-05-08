from rest_framework import serializers
from store.models import Store,Product


class DummySerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)

class StoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
