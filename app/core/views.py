from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from core import serializers
from rest_framework import status
from rest_framework.views import APIView


class EchoApiView(APIView):
    """Test API View"""
    serializer_class = serializers.EchoSerializer

    def get(self, request, name):
        """Returns a list of APIView features"""
        return Response(
            {'message': 'APIView', 'method': request.method, 'query': request.query_params.get("id"), 'param': name,
             'token': request.META.get("HTTP_TOKEN")})

    def post(self, request, name):
        """Returns a list of APIView features"""
        return Response(
            {'message': 'APIView', 'method': request.method, 'query': request.query_params.get("id"), 'param': name,
             'token': request.META.get("HTTP_TOKEN")})

    def put(self, request, name):
        """Returns a list of APIView features"""
        return Response(
            {'message': 'APIView', 'method': request.method, 'query': request.query_params.get("id"), 'param': name,
             'token': request.META.get("HTTP_TOKEN")})

    def patch(self, request, name):
        """Returns a list of APIView features"""
        return Response(
            {'message': 'APIView', 'method': request.method, 'query': request.query_params.get("id"), 'param': name,
             'token': request.META.get("HTTP_TOKEN")})

    def delete(self, request, name):
        """Returns a list of APIView features"""
        return Response(
            {'message': 'APIView', 'method': request.method, 'query': request.query_params.get("id"), 'param': name,
             'token': request.META.get("HTTP_TOKEN")})


class EchoViewSet(ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.EchoSerializer

    def list(self, request, *args, **kwargs):
        """Return a hello message"""
        return Response({'message': 'ViewSet', 'method': request.method,
                         'query': request.query_params.get("id", False),
                         'param': kwargs.get("name", False), 'token': request.META.get("HTTP_TOKEN")})

    # def create(self, request, *args, **kwargs):
    #     """Return a hello message"""
    #     return Response({'message': 'ViewSet', 'method': request.method, 'query': request.query_params.get("id"),
    #                      'param': kwargs.get("name", False), 'token': request.META.get("HTTP_TOKEN")})

    # def create(self, request):
    #     """Create a new hello message"""
    #     serializer = self.serializer_class(data=request.data)
    #
    #     if serializer.is_valid():
    #         name = serializer.validated_data.get('name')
    #         message = f'Hello {name}!'
    #         return Response({'message': message})
    #     else:
    #         return Response(
    #             serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    # def retrieve(self, request, pk=None):
    #     """Handle getting an object by its ID"""
    #     return Response({'http_method': 'GET'})
    #
    # def update(self, request, pk=None):
    #     """Handle a updating an object"""
    #     return Response({'http_method': 'PUT'})
    #
    # def partial_update(self, request, pk=None):
    #     """Handle updating part of an object"""
    #     return Response({'http_method': 'PATCH'})
    #
    # def destroy(self, request, pk=None):
    #     """handle removing an object"""
    #     return Response({'http_method': 'DELETE'})
