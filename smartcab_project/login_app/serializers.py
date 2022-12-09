
from rest_framework import serializers
from .models import login
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

 # Serializer to Get User Details using Django Token Authentication
class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = ["username", "mail_id", "password"]