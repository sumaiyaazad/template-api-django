from rest_framework.response import Response
from rest_framework import viewsets
from core import serializers
from rest_framework import status
from rest_framework.views import APIView


class EchoApiView(APIView):
    """Test API View"""
    serializer_class = serializers.EchoSerializer

    def get(self, request, name):
        """Returns a list of APIView features"""
        return Response({'message': f'Echo Api param: {name} query: {request.query_params.get("id")}'})


class EchoViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.EchoSerializer

    def list(self):
        """Return a hello message"""
        print("view-set  ")
        print(self.request.query_params.get('name', False))
        # print(request.query_params)
        return Response({'message': 'Echo View'})


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
