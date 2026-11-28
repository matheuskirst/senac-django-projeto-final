from django.db import models

from .shipment import Shipment
from .purchase_order_item import PurchaseOrderItem

class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment)
    order_item = models.ForeignKey(PurchaseOrderItem, null=True, on_delete=models.SET_NULL)
    received_quantity = models.IntegerField()
