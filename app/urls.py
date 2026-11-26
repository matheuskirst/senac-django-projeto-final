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

    path("personnel/", views.personnel, name="personnel"),
    path("register-employee/", views.register_product, name="register-employee"),

    path("inventory/", views.inventory, name="inventory"),
    path("register-product/", views.register_product, name="register-product")
]
