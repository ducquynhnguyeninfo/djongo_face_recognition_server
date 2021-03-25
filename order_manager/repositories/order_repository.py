from order_manager.shared import Singleton, DataRepository
from order_manager.models.order import Order
from order_manager.modelserializer.order import OrderSerializer

class OrderRepository(DataRepository):

    def getAll(self):
        return Order.objects.all()

    def get_by_name(self, name: str):
        result = Order.objects.filter(name = name)
        return result

    def get_by_pk(self, pk: str):
        result = Order.objects.get(pk = pk)
        return result
    
    def create(self, serializer: OrderSerializer):
        serializer.save()
        return serializer
        
    def update(self, newdata: OrderSerializer):
        newdata.save()
        return newdata

    def delete(self, pk):
        target = self.get_by_pk(pk)
        target.delete()