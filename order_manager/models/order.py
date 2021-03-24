# Create your models here.
import uuid
from django.utils import timezone

from djongo import models
from rest_framework import serializers

from order_manager.models.brand import Brand
from order_manager.models.vehicle_model import VehicleModel


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=200)
    created_at = models.DateTimeField('created time', default=timezone.now, editable=False)
    last_modified_at = models.DateTimeField('last modified time')
    total_money = models.FloatField(default=0, )

    def __str__(self):
        return self.client_name


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = ('id', 'client_name', 'created_at', 'last_modified_at', 'total_money')
