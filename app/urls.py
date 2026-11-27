from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import AppAuthenticationForm

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="login.html",
        authentication_form=AppAuthenticationForm,
        redirect_authenticated_user = True
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("", views.DashboardView.as_view(), name="dashboard"),

    path("personnel/", views.PersonnelView.as_view(), name="personnel"),
    path("register-employee/", views.RegisterEmployeeView.as_view(), name="register-employee"),

    path("inventory/", views.InventoryView.as_view(), name="inventory"),
    path("register-product/", views.RegisterProductView.as_view(), name="register-product")
]
