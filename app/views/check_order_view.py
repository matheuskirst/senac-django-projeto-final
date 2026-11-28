from django.views.generic import TemplateView

class CheckOrderView(TemplateView):
    template_name = "pages/operator/check-order.html"
