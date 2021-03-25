import uuid

from django.db import models
from rest_framework import serializers
from order_manager.models.brand import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'description', 'vehiclemodels')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": True,
            },
        }

    vehiclemodels = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    description = serializers.CharField(allow_blank=True)
    id = serializers.UUIDField(read_only=True)