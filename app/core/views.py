from rest_framework.response import Response
from rest_framework import viewsets
from core import serializers


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        return Response({'message': 'Hello'})
