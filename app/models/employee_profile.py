from django.conf import settings
from django.db import models

class EmployeeProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, error_messages={'unique': 'Este CPF já está cadastrado.'})
    date_of_birth = models.DateField()

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile"
    )
