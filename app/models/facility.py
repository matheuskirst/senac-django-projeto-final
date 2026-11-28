from django.db import models

from .employee_profile import EmployeeProfile

class Facility(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    manager = models.ForeignKey(EmployeeProfile, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
