from django.http.response import Http404
from django import http

from order_manager.shared import Singleton, DataRepository
from order_manager.models.brand import Brand, BrandSerializer
from order_manager.repositories import BrandRepository
from order_manager.services.base_service import BaseService

# from django.http import Http404


class BrandService():

    def __init__(self, repository: DataRepository):
        super().__init__()
        self.repository = repository

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get_all(self):
        brands = self.repository.getAll()
        serializer = BrandSerializer(brands, many=True)
        return serializer

    def get_by_name(self, name: str):
        try:
            brands = self.repository.get_by_name(name)
            serializer = BrandSerializer(brands, many=True)
            return serializer
        except Brand.DoesNotExist:
            raise http.Http404

    def get_by_pk(self, pk: str):
        try:
            brand = self.repository.get_by_pk(pk)
            serializer = BrandSerializer(brand)
            return serializer
        except Brand.DoesNotExist:
            raise http.Http404
            # return httHttp404

    def create(self, data: any):
        try:
            serializer = BrandSerializer(data=data)
            if serializer.is_valid():
                return self.repository.create(serializer)
            raise Exception('data is not valid')
        except Exception as e:
            raise e

    def update(self, newdata: any, pk: str):
        try:
            old = self.repository.get_by_pk(pk)
            serializer = BrandSerializer(old, data=newdata)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return serializer
            raise Exception('data is not valid')
        except Exception as e:
            raise e

    def delete(self, pk):
        self.repository.delete(pk)
