from django.db import models

class Operator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, error_messages={'unique': 'Este CPF já está cadastrado.'})
    birthdate = models.DateField()
