from django import forms

from ..models import Product

class RegisterEmployeeForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'unit_cost',
            'selling_price',
            'reorder_point',
            'supplier',
        ]
