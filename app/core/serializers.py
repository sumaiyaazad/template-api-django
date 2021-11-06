
from rest_framework import serializers


class EchoSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    id = serializers.DecimalField(max_digits=2, decimal_places=0)