
from order_manager.shared import Singleton, DataRepository
from django.http.response import Http404
from django import http
from order_manager.models.order import Order, OrderSerializer
from order_manager.models.vehicle_model import VehicleModel, VehicleModelSerializer


class MiscService():

    def __init__(self):
        super().__init__()
        self.repository = repository

    def get_of_brand(self, brandId: str):
        try:
            obj_set = self.repository.get (brandId)
            serializer = VehicleModelSerializer(obj_set, many=True)
            return serializer
        except VehicleModel.DoesNotExist:
            raise http.Http404
            # return httHttp404
