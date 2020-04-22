from django.shortcuts import render
from forms.serializers import FormSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class FormViewSet(APIView):
    def post(self, request, format=None):
        serializer = FormSerializers(data=request.data)
        return Response('Valid') if serializer.is_valid() else Response(serializer.errors)
