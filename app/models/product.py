from django.db import models

from .supplier import Supplier

class Product(models.Model):
    sku = models.CharField("SKU", max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    unit_cost = models.FloatField()
    selling_price = models.FloatField()
    reorder_point = models.IntegerField()

    supplier = models.ManyToManyField(Supplier)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
