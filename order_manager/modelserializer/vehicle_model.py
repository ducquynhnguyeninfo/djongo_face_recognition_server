import uuid

from django.db import models
from rest_framework import serializers
from order_manager.models.brand import Brand
from order_manager.models.vehicle_model import VehicleModel
from order_manager.modelserializer.brand import BrandSerializer

class VehicleModelSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200, allow_blank=False)
    price = serializers.FloatField(default=0, min_value=0)
    description = serializers.CharField(max_length=256, allow_blank=True)
    brand = BrandSerializer()

    class Meta:
        model = VehicleModel
        fields = ('id', 'name', 'description', 'price', 'brand')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": True,
            },
        }

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
        # why data passing from service lost??????//
        print(validated_data)

        instance = VehicleModel()
        # brand_data = validated_data.pop('brand')

        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        brand = validated_data.get('brand')
        brand_id = brand.get('id')
        instance.brand_id = brand_id
        # brand = Brand(id=brand_data.id, name=brand_data.name, description=brand_data.description)
        # brand = Brand()
        # brand.id = brand_data.get('id', brand.id)
        # brand.name = brand_data.get('name', brand.name)
        # brand.description = brand_data.get('description', brand.description)
        
        # instance.brand = brand
        instance.save()
        return instance
        # return super().create(validated_data)


    # def is_valid(self, raise_exception=False):
    #     # return super().is_valid(raise_exception=raise_exception)
    #     self._validated_data = True
    #     super().is_valid(raise_exception=raise_exception)

    #     return True