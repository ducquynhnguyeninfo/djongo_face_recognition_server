from order_manager.shared import Singleton, DataRepository
from django.http.response import Http404
from django import http
from order_manager.models.order import Order, OrderSerializer


class OrderService():

    def __init__(self, repository: DataRepository):
        super().__init__()
        self.repository = repository

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get_all(self):
        obj_set = self.repository.getAll()
        serializer = OrderSerializer(obj_set, many=True)
        return serializer

    def get_by_name(self, name: str):
        try:
            obj_set = self.repository.get_by_name(name)
            serializer = OrderSerializer(obj_set, many=True)
            return serializer
        except Order.DoesNotExist:
            raise http.Http404

    def get_by_pk(self, pk: str):
        try:
            obj_set = self.repository.get_by_pk(pk)
            serializer = OrderSerializer(obj_set)
            return serializer
        except Order.DoesNotExist:
            raise http.Http404
            # return httHttp404

    def create(self, data: any):
        try:
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                return self.repository.create(serializer)
            raise Exception('data is not valid')
        except Exception as e:
            raise e
            
    def update(self, newdata: any, pk: str):
        try:
            old = self.repository.get_by_pk(pk)
            serializer = OrderSerializer(old, data=newdata)
            if serializer.is_valid(raise_exception=True):
                return self.repository.update(serializer)
            raise Exception('data is not valid')
        except Exception as e:
            raise e

    def delete(self, pk):
        self.repository.delete(pk)
