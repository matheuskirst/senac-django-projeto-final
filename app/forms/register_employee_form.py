from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from ..models import EmployeeProfile

class RegisterEmployeeForm(forms.ModelForm):
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        empty_label="Selecione um cargo."
    )

    # roles = forms.ModelMultipleChoiceField(
    #     queryset=Group.objects.all(),
    #     required=True,
    #     widget=forms.CheckboxSelectMultiple,
    # )

    class Meta:
        model = EmployeeProfile
        fields = [
            'first_name',
            'last_name',
            'cpf',
            'date_of_birth',
            'password',
            'confirm_password',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                self.add_error("confirm_password", "As senha não coincidem.")
            else:
                User = get_user_model()
                candidate_user = User(
                    username=cleaned_data.get("cpf"),
                    first_name=cleaned_data.get("first_name"),
                    last_name=cleaned_data.get("last_name"),
                )

                try:
                    validate_password(password, candidate_user)
                except ValidationError as error:
                    self.add_error("password", error)

        return cleaned_data
