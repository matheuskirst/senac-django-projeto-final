from django.db import models

from ..supplier import Supplier
from ...enums import PurchaseOrderStatus

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    status = models.IntegerField(choices=PurchaseOrderStatus.choices)

    order_date = models.DateTimeField(auto_now_add=True)
