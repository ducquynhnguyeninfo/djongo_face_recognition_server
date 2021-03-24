
from order_manager.shared.singleton import Singleton
from abc import ABCMeta, abstractmethod

class DataRepository(object):

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass

    @abstractmethod
    def get_by_pk(self, pk: str):
        pass

    @abstractmethod
    def create(self, serializer: any):
        pass
    
    @abstractmethod
    def update(self, newdata: any):
        pass
    
    @abstractmethod
    def delete(self, pk):
        pass