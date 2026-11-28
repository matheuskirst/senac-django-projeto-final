from django.views.generic import TemplateView

class InventoryView(TemplateView):
    template_name = "pages/manager/inventory.html"
