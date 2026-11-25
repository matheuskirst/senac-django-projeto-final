from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission

from app.groups import ADMIN_GROUP, OPERATOR_GROUP

class Command(BaseCommand):
    help = "Create app groups"

    def handle(self, *args, **options):
        try:
            Group.objects.get_or_create(name=OPERATOR_GROUP)
            Group.objects.get_or_create(name=ADMIN_GROUP)
            self.add_admin_permissions()
        except Exception as e:
            print(f'Database error: {e}')

    def add_admin_permissions(self):
        try:
            admin_group = Group.objects.get(name=ADMIN_GROUP)
            codenames = ['view_employeeprofile', 'add_employeeprofile', 'change_employeeprofile', 'delete_employeeprofile']
            permissions = Permission.objects.filter(content_type__app_label='app', codename__in=codenames)
            for permission in permissions.all():
                admin_group.permissions.add(permission)
        except Exception as e:
            print(f'Database error: {e}')
