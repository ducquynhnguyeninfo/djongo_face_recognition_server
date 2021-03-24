import uuid

from django.db import models
from rest_framework import serializers

from order_manager.models.brand import Brand, BrandSerializer


class VehicleModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True)
    picture = models.CharField(max_length=256, blank=True)
    price = models.FloatField(default=0)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.name} -  {self.price}'


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ('id', 'name', 'picture', 'price', 'brand')
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=200, allow_blank=False)
    picture = serializers.CharField(max_length=256, allow_blank=True)
    price = serializers.FloatField(default=0, min_value=0)
    brand = BrandSerializer()
    # brand = serializers.PrimaryKeyRelatedField(read_only=True)

    def update(self, instance, validated_data):
        print(instance)
        print(validated_data) 

        brand_data = validated_data.pop('brand')
        brand = instance.brand

        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        brand.id = brand_data.get('id', brand.id)
        brand.name = brand_data.get('name', brand.name)
        brand.description = brand_data.get('description', brand.description)
        brand.save()
        
        return instance
    
    
    def create(self, validated_data):

        print(validated_data)

        return super().create(validated_data)


    # def is_valid(self, raise_exception=False):
    #     # return super().is_valid(raise_exception=raise_exception)
    #     self._validated_data = True
    #     super().is_valid(raise_exception=raise_exception)

    #     return True