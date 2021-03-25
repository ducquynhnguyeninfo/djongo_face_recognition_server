# Create your models here.
import uuid

from djongo import models
from rest_framework import serializers

from order_manager.models import Order
from order_manager.models.vehicle_model import VehicleModel 


class Pack(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    model = models.ManyToManyField(VehicleModel)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.model.vehiclemodel.brand
