from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from core import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action


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
             'token': request.META.get("HTTP_TOKEN"), 'body': request.data})

    def put(self, request, name):
        """Returns a list of APIView features"""
        return Response(
            {'message': 'APIView', 'method': request.method, 'query': request.query_params.get("id"), 'param': name,
             'token': request.META.get("HTTP_TOKEN"), 'body': request.data})

    def patch(self, request, name):
        """Returns a list of APIView features"""
        return Response(
            {'message': 'APIView', 'method': request.method, 'query': request.query_params.get("id"), 'param': name,
             'token': request.META.get("HTTP_TOKEN"), 'body': request.data})

    def delete(self, request, name):
        """Returns a list of APIView features"""
        return Response(
            {'message': 'APIView', 'method': request.method, 'query': request.query_params.get("id"), 'param': name,
             'token': request.META.get("HTTP_TOKEN")})


class EchoViewSet(ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.EchoSerializer

    # defined update(put) and partial_update(patch) do not take any query
    # defined create(post) does not take any param or query

    def list(self, request, *args, **kwargs):
        """Return a hello message"""
        return Response({'message': 'ViewSet', 'method': request.method,
                         'query': request.query_params.get("id", False),
                         'param': kwargs.get("name", False), 'token': request.META.get("HTTP_TOKEN")})

    def create(self, request):
        """Create a new hello message"""
        return Response({'message': 'ViewSet', 'method': request.method, 'token': request.META.get("HTTP_TOKEN"), 'body': request.data})

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'message': 'ViewSet', 'method': request.method, 'query': request.query_params.get("id", False),
                         'param': pk, 'token': request.META.get("HTTP_TOKEN")})

    def update(self, request, pk=None):
        """Handle a updating an object"""
        return Response({'message': 'ViewSet', 'method': request.method, 'query': request.query_params.get("id", False),
                         'param': pk, 'token': request.META.get("HTTP_TOKEN"), 'body': request.data})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'message': 'ViewSet', 'method': request.method, 'query': request.query_params.get("id", False),
                         'param': pk, 'token': request.META.get("HTTP_TOKEN"), 'body': request.data})

    def destroy(self, request, pk=None):
        """handle removing an object"""
        return Response({'message': 'ViewSet', 'method': request.method, 'query': request.query_params.get("id", False),
                         'param': pk, 'token': request.META.get("HTTP_TOKEN")})


class EchoModelViewSet(ViewSet):

    @action(detail=True, methods=['get', 'post', 'put', 'patch', 'delete'])
    def details(self, request, pk=None):
        """Return a hello message"""
        return Response({'message': 'ViewSet', 'method': request.method,
                         'query': request.query_params.get("id", False),
                         'param': pk, 'token': request.META.get("HTTP_TOKEN"), 'body': request.data})
