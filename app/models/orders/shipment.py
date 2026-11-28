from django.db import models

from ..supplier import Supplier
from .purchase_order import PurchaseOrder
from ...enums import ShipmentStatus

class Shipment(models.Model):
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(PurchaseOrder)
    tracking_number = models.CharField(max_length=128)
    status = models.IntegerField(choices=ShipmentStatus.choices)

    received_date = models.DateTimeField()
