# Create your models here.
import uuid

from djongo import models
from rest_framework import serializers

from order_manager.models import Order
from order_manager.models.vehicle_model import VehicleModel 

class PackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pack
        fields = ('id', 'order', 'model', 'price', 'quantity')
