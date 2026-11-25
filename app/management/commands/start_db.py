from django.core import management
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "Bootstrap database with the app defined groups and an admin superuser. Calls 'create_groups' and 'auto_createsuperuser'"

    def handle(self, *args, **options):
        management.call_command('create_groups')
        management.call_command('auto_createsuperuser')
