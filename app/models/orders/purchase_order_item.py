from django.db import models

from ..product import Product
from .purchase_order import PurchaseOrder

class PurchaseOrderItem(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
