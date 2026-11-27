from django import forms

from ..models import Supplier

class RegisterSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'company_name',
            'contact_name',
            'email',
            'phone_number',
            'payment_terms',
        ]
