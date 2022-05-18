# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

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
