from rest_framework import serializers
from django.conf import settings
import requests
import re


class FormSerializers(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField()
    fname = serializers.CharField(required=False)
    lname = serializers.CharField(required=False)
    cardn = serializers.CharField(min_length=16, max_length=16)

    def validate_phone(self, value):
        if re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", value) == None:
            raise serializers.ValidationError("There must be valid phone number")
        return value

    def validate_cardn(self, value):
        import pdb
        pdb.set_trace()
        if not value.isdecimal():
            raise serializers.ValidationError("card number is not valid")
        api_key = getattr(settings, 'CARD_INFO_API_KEY', None)
        allowed_banks = getattr(settings, 'ALLOWED_BANKS', [])
        request = requests.get(f"https://api.cardinfo.online/?input={value[0:6]}&apiKey={api_key}")
        if request.json().get('bankName', False) not in allowed_banks:
            raise serializers.ValidationError("Bank is not in allowed banks")
        return value
