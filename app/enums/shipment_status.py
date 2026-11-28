from django.db import models

class ShipmentStatus(models.IntegerChoices):
    SENT = 1, "Enviado"
    IN_TRANSIT = 2, "Em transito"
    ARRIVED = 3, "Completo"
