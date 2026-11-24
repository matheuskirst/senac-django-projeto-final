from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from app.forms.cpf_authentication_form import CpfAuthenticationForm

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", LoginView.as_view(
        template_name="login.html",
        authentication_form=CpfAuthenticationForm,
        # redirect_authenticated_user = True
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("operators/", views.operators, name="operators"),
    path("new-operator/", views.new_operator, name="new-operator"),
    path("inventory/", views.inventory, name="inventory"),
]
