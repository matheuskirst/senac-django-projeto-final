from django.db import models

class PurchaseOrderStatus(models.IntegerChoices):
    SENT = 1, "Enviado"
    PARTIAL = 2, "Parcial"
    COMPLETED = 3, "Completo"
