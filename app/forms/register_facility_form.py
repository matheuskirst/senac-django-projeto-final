from django import forms

from ..models import Facility

class RegisterFacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = [
            'name',
            'address',
            'manager',
        ]
