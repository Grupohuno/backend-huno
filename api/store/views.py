from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

import store.serializers as serializers

class DummyView(APIView):

    def get(self, request, *args, **kwargs):
        obj = {
            "name": "object 1",
            "store":1,
            "category": "beer",
        }
        serializer=serializers.ResponseSerializer(data=obj)
        if serializer.is_valid():
            print("Valido el Serialiers")
            return Response(obj)

        else:
            return Response({})

