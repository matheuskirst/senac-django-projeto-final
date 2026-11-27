from django import forms

from ..models import InventoryFacility

class RegisterInventoryFacilityForm(forms.ModelForm):
    class Meta:
        model = InventoryFacility
        fields = [
            'name',
            'address',
            'capacity',
            'manager',
        ]
