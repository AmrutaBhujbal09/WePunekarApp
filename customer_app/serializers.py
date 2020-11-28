from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Customer


class CustomerSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "password", "username", "email", "contact_number",
                  "status","type_c","pincode"]

    def create(self,validated_data):
        customer = Customer.objects.create_user(
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            password=validated_data.pop('password'),
            contact_number=validated_data.pop('contact_number'),
            #aadhar_card=validated_data.pop('aadhar_card'),
            #address=validated_data.pop('address'),
            status=validated_data.pop('status'),
            type_c=validated_data.pop('type_c'),

            #  first_name=validated_data.pop('first_name') i.e in html form first_name take rquested data & put in first_name i.e put
            # under column name as first_name in Customer model .

        )
        return customer


class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    type_user= serializers.CharField(required=True)

    def validate(self,attrs):
        self.user = authenticate(username=attrs.pop("email"), password=attrs.pop("password"),type_c=attrs.pop("type_user"))

        if self.user:
            return attrs

        else:
            raise serializers.ValidationError()


class CustomerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields:["id","first_name","last_name","email","contact_number"]

