from django.views.generic import TemplateView

class RegisterEmployeeView(TemplateView):
    template_name = "register-employee.html"
