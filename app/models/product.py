from django.db import models

class Product(models.Model):
    sku = models.CharField("SKU", max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    reorder_point = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
