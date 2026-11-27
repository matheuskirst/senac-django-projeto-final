from django import forms

from ..models import InventoryFacility

class RegisterEmployeeForm(forms.ModelForm):
    class Meta:
        model = InventoryFacility
        fields = [
            'name',
            'address',
            'capacity',
            'manager',
        ]
