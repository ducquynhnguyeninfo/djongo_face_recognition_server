from django.http import HttpRequest, JsonResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.decorators import api_view, api

from order_manager.models.brand import *
from order_manager.services import *


class BrandList(APIView):
    """
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = brandService

    def get(self, request: HttpRequest, format=None):
        """ Retrieve all brand names """
        serializer = self.service.get_all()
        return Response(serializer.data)

    def post(self, request: HttpRequest, format=None):
        """ Create new brand """

        serializer = self.service.create(data=request.data)
        if (serializer != None):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetail(APIView):
    """
        To handle all requests CRUD of brand
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = brandService

    def get(self, request, pk, format=None):
        serializer = self.service.get_by_pk(pk)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        serializer = self.service.update(newdata=request.data, pk=pk)

        if (serializer != None):
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.service.delete(pk)
    
        return Response(status=status.HTTP_204_NO_CONTENT)
