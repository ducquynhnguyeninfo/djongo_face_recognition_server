from order_manager.shared import Singleton, DataRepository
from order_manager.models.brand import Brand, BrandSerializer
from order_manager.repositories import BrandRepository
from django.http.response import Http404
# from django.http import Http404
from django import http


class BaseService():

    def __init__(self, repository: DataRepository, classType: type, serializerType: type):
        super().__init__()
        self.repository = repository
        self.modelType = classType
        self.serializerType = serializerType

    def get_class(self, cls: str):
        parts = cls.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m

    def get_object(self, pk):
        try:
            # self.get_class(self.modelType)
            return self.modelType.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get_all(self):
        brands = self.repository.getAll()
        serializer = self.serializerType(brands, many=True)
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
                serializer.save()
                return serializer
            raise None
        except:
            return None

    def update(self, newdata: any, pk: str):
        try:
            old = self.repository.get_by_pk(pk)
            serializer = BrandSerializer(old, data=newdata)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return serializer
        except Exception as e:
            raise e

    def delete(self, pk):
        self.repository.delete(pk)
