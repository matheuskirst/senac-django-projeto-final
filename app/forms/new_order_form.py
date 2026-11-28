from django import forms

from ..models.orders import PurchaseOrder

class NewOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = [
            'supplier',
            'status',
        ]
