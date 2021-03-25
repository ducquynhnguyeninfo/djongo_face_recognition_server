from order_manager.shared import Singleton, DataRepository
from order_manager.models.brand import Brand
from order_manager.modelserializer.brand import BrandSerializer

class BrandRepository(DataRepository):

    def getAll(self):
        return Brand.objects.all()

    def get_by_name(self, name: str):
        result = Brand.objects.filter(name = name)
        return result

    def get_by_pk(self, pk: str):
        result = Brand.objects.get(pk = pk)
        return result

    def get_by_pk(self, pk: str):
        result = Brand.objects.get(pk = pk)
        return result
    
    def create(self, serializer: BrandSerializer):
        
        serializer.save()
        return serializer
        
    def update(self, newdata: BrandSerializer):
        newdata.save()
        return newdata

    def delete(self, pk):
        target = self.get_by_pk(pk)
        target.delete()

