from matplotlib import category
from rest_framework import serializers

class ResponseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    store = serializers.PrimaryKeyRelatedField()
    category = serializers.CharField(max_length=200)