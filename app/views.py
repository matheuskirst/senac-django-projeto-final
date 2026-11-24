from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_not_required

from app.decorators import group_required
from .groups import ADMIN_GROUP, OPERATOR_GROUP

@group_required(ADMIN_GROUP, OPERATOR_GROUP)
def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'dashboard.html')

@group_required(ADMIN_GROUP)
def operators(request: HttpRequest) -> HttpResponse:
    return render(request, 'operators.html')

@group_required(ADMIN_GROUP)
def register_operator(request: HttpRequest) -> HttpResponse:
    return render(request, 'register-operator.html')

@group_required(ADMIN_GROUP, OPERATOR_GROUP)
def inventory(request: HttpRequest) -> HttpResponse:
    return render(request, 'inventory.html')

@group_required(ADMIN_GROUP)
def create_product(request: HttpRequest) -> HttpResponse:
    return render(request, 'create-product.html')
