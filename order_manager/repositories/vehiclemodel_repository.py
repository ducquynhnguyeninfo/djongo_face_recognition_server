from order_manager.shared import Singleton, DataRepository
from order_manager.models.vehicle_model import VehicleModel, VehicleModelSerializer

class VehicleModelRepository(DataRepository):

    def getAll(self):
        return VehicleModel.objects.all()

    def get_by_name(self, name: str):
        result = VehicleModel.objects.filter(name = name)
        return result

    def get_by_pk(self, pk: str):
        result = VehicleModel.objects.get(pk = pk)
        return result
    
    def create(self, serializer: VehicleModelSerializer):
        
        serializer.save()
        return serializer
        
    def update(self, newdata: VehicleModelSerializer):
        newdata.save()
        return newdata

    def delete(self, pk):
        target = self.get_by_pk(pk)
        target.delete()

