from rest_framework import serializers


class ResponseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    store = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.CharField(max_length=200)
