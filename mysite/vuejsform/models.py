from django.db import models
from django.utils import timezone

class Product(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=10)
    factory = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
