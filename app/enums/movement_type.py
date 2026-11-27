from django.db import models

class MovementType(models.IntegerChoices):
    RECEIVED_FROM_SUPPLIER = 1, "Recebido de fornecedor"
    SHIPPER_TO_COSTUMER = 2, "Enviado para cliente"
    TRANSFERRED = 3, "Transferência"
    ADJUSTED = 4, "Ajuste"
