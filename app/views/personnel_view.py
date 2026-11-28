from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin

from ..models import EmployeeProfile

class PersonnelView(PermissionRequiredMixin, TemplateView):
    template_name = "pages/administrator/personnel.html"
    permission_required = "app.view_employeeprofile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roles = Group.objects.all()
        personnel = EmployeeProfile.objects.all()
        
        search_field = self.request.GET.get(key="search", default="").strip()
        filter_roles = self.request.GET.get(key="roles", default="")

        last_search = {
            "search_field": search_field,
            "role": filter_roles
        }

        personnel = personnel.filter(
            Q(first_name__icontains=search_field)
            |Q(last_name__icontains=search_field)
            |Q(cpf__contains=search_field)
        )

        try:
            personnel = personnel.filter(user__groups__pk=int(filter_roles))
        except:
            pass

        context["roles"] = roles
        context["personnel"] = personnel
        context["search"] = last_search
        return context
