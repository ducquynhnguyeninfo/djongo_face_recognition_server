import uuid

from django.db import models
from rest_framework import serializers
from order_manager.models.brand import Brand

class VehicleModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=256, blank=True, default="")
    price = models.FloatField(default=0)

    brand = models.ForeignKey(Brand, related_name='vehiclemodels', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
