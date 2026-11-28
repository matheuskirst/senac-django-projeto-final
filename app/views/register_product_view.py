from django.views.generic import TemplateView

class RegisterProductView(TemplateView):
    template_name = "pages/manager/register-product.html"
