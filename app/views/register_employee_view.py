from django.views.generic import TemplateView

class RegisterEmployeeView(TemplateView):
    template_name = "pages/administrator/register-employee.html"
