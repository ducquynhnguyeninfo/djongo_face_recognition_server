# Create your models here.
import uuid
from django.utils import timezone

from djongo import models
from rest_framework import serializers

from order_manager.models.order import Order
# from order_manager.models.vehicle_model import VehicleModel

class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = ('id', 'client_name', 'created_at', 'last_modified_at', 'total_money')
