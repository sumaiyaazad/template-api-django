# from django.contrib.auth import get_user_model
from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['email']


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)