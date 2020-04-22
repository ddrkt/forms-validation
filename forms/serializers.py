from rest_framework import serializers
import re


class FormSerializers(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField()
    fname = serializers.CharField()
    lname = serializers.CharField()

    def validate_phone(self, value):
        if re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", value) == None:
            raise serializers.ValidationError("There must be valid phone number")
        return value
