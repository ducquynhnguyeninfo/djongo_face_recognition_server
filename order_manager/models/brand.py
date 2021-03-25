import uuid

from django.db import models
from rest_framework import serializers

class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name
