from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db import transaction
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .decorators import group_required
from .forms import RegisterEmployeeForm
from .groups import ADMIN_GROUP, OPERATOR_GROUP
from .models import EmployeeProfile

@group_required(ADMIN_GROUP, OPERATOR_GROUP)
def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'dashboard.html')

@group_required(ADMIN_GROUP)
def operators(request: HttpRequest) -> HttpResponse:
    return render(request, 'personnel.html')

@group_required(ADMIN_GROUP)
def new_employee(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        employee_form = RegisterEmployeeForm(request.POST)

        if employee_form.is_valid():
            User = get_user_model()

            with transaction.atomic():
                employee: EmployeeProfile = employee_form.save(commit=False)

                user = User.objects.create_user(
                    username=employee.cpf,
                    password=employee_form.cleaned_data['password'],
                    is_employee=True
                )

                employee.user = user
                employee.save()
                user.groups.add(Group.objects.get(name=OPERATOR_GROUP))

    return render(request, 'new-employee.html')

@group_required(ADMIN_GROUP, OPERATOR_GROUP)
def inventory(request: HttpRequest) -> HttpResponse:
    return render(request, 'inventory.html')

@group_required(ADMIN_GROUP)
def create_product(request: HttpRequest) -> HttpResponse:
    return render(request, 'create-product.html')
