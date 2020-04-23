from django.shortcuts import render
from forms.serializers import FormSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


# Create your views here.

class FormViewSet(APIView):
    def post(self, request, format=None):
        serializer = FormSerializers(data=request.data)
        if serializer.is_valid():
            return Response(dict(result="input is valid"))
        raise ValidationError(serializer.errors, 400)
