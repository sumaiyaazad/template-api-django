# from django.contrib.auth import get_user_model
# from rest_framework import viewsets
# from core.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from core import serializers


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class HelloViewSet(APIView):
#     """Test API View"""
#     serializer_class = serializers.HelloSerializer
#
#     def get(self, request, format=None):
#         """Returns a hello message"""
#
#         return Response({'message': 'Hello!'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        return Response({'message': 'Hello'})
