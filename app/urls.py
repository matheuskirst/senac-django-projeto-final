from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import AppAuthenticationForm

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", LoginView.as_view(
        template_name="login.html",
        authentication_form=AppAuthenticationForm,
        redirect_authenticated_user = True
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("personnel/", views.operators, name="personnel"),
    path("new-employee/", views.new_employee, name="new-employee"),
    path("inventory/", views.inventory, name="inventory"),
    path("create-product/", views.create_product, name="create-product")
]
