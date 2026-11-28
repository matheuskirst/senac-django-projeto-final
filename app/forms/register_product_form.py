from django import forms

from ..models import Product

class RegisterProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'reorder_point',
        ]
