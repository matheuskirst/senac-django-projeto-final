from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db import transaction
from django.db.models import Q
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
def personnel(request: HttpRequest) -> HttpResponse:
    search_field = request.GET.get(key="search", default="").strip()
    selected_roles = request.GET.get(key="roles", default="")

    last_search = {
        "search_field": search_field,
        "role": selected_roles
    }

    roles = Group.objects.all()

    personnel = EmployeeProfile.objects.all()
    personnel = personnel.filter(
        Q(first_name__icontains=search_field)
        | Q(last_name__icontains=search_field)
        | Q(cpf__contains=search_field)
    )

    try:
        personnel = personnel.filter(user__groups__pk=int(selected_roles))
    except:
        pass

    context = {
        "personnel": personnel,
        "roles": roles,
        "search": last_search
    }

    return render(request, 'personnel.html', context)

@group_required(ADMIN_GROUP)
def register_employee(request: HttpRequest) -> HttpResponse:
    groups = Group.objects.all()

    if request.method == 'GET':
        employee_form = RegisterEmployeeForm()

        context = {
            "form": employee_form,
            "roles": groups
        }

        return render(request, 'new-employee.html', context)

    if request.method == 'POST':
        employee_form = RegisterEmployeeForm(request.POST)

        if employee_form.is_valid():
            User = get_user_model()

            with transaction.atomic():
                employee: EmployeeProfile = employee_form.save(commit=False)

                user = User.objects.create_user(
                    username=employee.cpf,
                    password=employee_form.cleaned_data['password'],
                    is_employee=True,
                )

                employee.user = user
                employee.save()
                user.groups.add(Group.objects.get(name=OPERATOR_GROUP))

            return redirect(to='personnel')

        context = {
            "form": employee_form,
            "roles": groups
        }
        return render(request, 'register-employee.html', context)

@group_required(ADMIN_GROUP, OPERATOR_GROUP)
def inventory(request: HttpRequest) -> HttpResponse:
    return render(request, 'inventory.html')

@group_required(ADMIN_GROUP)
def register_product(request: HttpRequest) -> HttpResponse:
    return render(request, 'register-product.html')
