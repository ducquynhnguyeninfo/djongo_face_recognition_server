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
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField()
    total_money = models.FloatField(default=0, )

    def __str__(self):
        return self.client_name