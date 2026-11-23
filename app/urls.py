from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from app.forms.CpfAuthenticationForm import CpfAuthenticationForm

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", LoginView.as_view(
        template_name="login.html",
        authentication_form=CpfAuthenticationForm,
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("operators/", views.operators, name="operators"),
    path("register-operator/", views.register_operator, name="register-operator"),
    path("inventory/", views.inventory, name="inventory"),
]
