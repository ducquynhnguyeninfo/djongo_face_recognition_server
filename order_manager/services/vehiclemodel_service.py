from django import http
from order_manager.shared import Singleton, DataRepository
from django.http.response import Http404
from order_manager.models.vehicle_model import VehicleModel
from order_manager.modelserializer.vehicle_model import VehicleModelSerializer
from rest_framework.request import Request
from django.http import HttpRequest
import uuid
from order_manager.models.brand import Brand
from order_manager.modelserializer.brand import BrandSerializer

class VehicleModelService():

    def __init__(self, repository: DataRepository):
        super().__init__()
        self.repository = repository

    def get_object(self, pk):
        try:
            return VehicleModel.objects.get(pk=pk)
        except VehicleModel.DoesNotExist:
            raise Http404

    def get_all(self, request: HttpRequest):
        obj_set = self.repository.getAll()
        serializer_context = {
            'request': request
        }
        serializer = VehicleModelSerializer(obj_set, many=True)
        return serializer

    def get_by_name(self, name: str):
        try:
            obj_set = self.repository.get_by_name(name)
            serializer = VehicleModelSerializer(obj_set, many=True)
            return serializer
        except VehicleModel.DoesNotExist:
            raise http.Http404

    def get_by_pk(self, pk: str):
        try:
            obj_set = self.repository.get_by_pk(pk)
            serializer = VehicleModelSerializer(obj_set)
            return serializer
        except VehicleModel.DoesNotExist:
            raise http.Http404
            # return httHttp404

    def create(self, data: any):
        try:
            # brand_data = data.pop('brand')
            rebuiltdata = data

            # rebuiltdata['brand'] = brand_data
            # brandserialized = self.repository.get_by_pk(pk=brand_id)
            serializer = VehicleModelSerializer(data=rebuiltdata)
            # serializer.brand = brandserialized
            # serializer.id = vm.id
            # serializer.name = data.get('name')
            # serializer.description = data.get('description')
            # serializer.price = data.get('price')
            # # b = Brand(id=uuid.uuid4())
            # serializer.brand = BrandSerializer(data=data.get('brand'))
            if serializer.is_valid():
                return self.repository.create(serializer=serializer)
            raise Exception(serializer.errors)
        except Exception as e:
            raise e

    def update(self, newdata: any, pk: str):
        try:
            old = self.repository.get_by_pk(pk)
            serializer = VehicleModelSerializer(old, data=newdata)
            newbrand = newdata.get('brand', {})
            serializer.brand = newbrand
            # serializer.brand_id = newbrand.id
            if serializer.is_valid(raise_exception=True):
                return self.repository.update(newdata=serializer)
            # raise Exception('data is not valid')
        except Exception as e:
            raise e

    def delete(self, pk):
        self.repository.delete(pk)
