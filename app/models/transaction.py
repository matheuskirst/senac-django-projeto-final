from django.db import models

from .product import Product
from .inventory_facility import InventoryFacility
from ..enums import MovementType

class Transaction(models.Model):
    facility = models.ForeignKey(InventoryFacility, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, to_field="sku", db_column="sku", null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    movement_type = models.IntegerField(choices=MovementType.choices)
    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
