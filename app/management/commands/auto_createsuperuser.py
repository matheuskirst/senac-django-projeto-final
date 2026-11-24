from dotenv import load_dotenv
import os
load_dotenv()

from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from app.groups import ADMIN_GROUP

class Command(BaseCommand):
    help = "Create a superuser and add it to the 'Admin' employee group. Use ADMIN_USERNAME and ADMIN_PASSWORD in your .env"

    def handle(self, *args, **options):
        ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
        print("Found Admin username")
        ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
        print("Found Admin password")

        User = get_user_model()
        print("Found project user model")

        superuser = User.objects.get(username=ADMIN_USERNAME)
        if superuser:
            print("Superuser already exists")
        else:
            print("Creating superuser")
            superuser = User.objects.create_superuser(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)

            Group.objects.get_or_create(name=ADMIN_GROUP)

            admin_group = Group.objects.get(name=ADMIN_GROUP)
            print(f"Found group '{ADMIN_GROUP}'")

            superuser.groups.add(admin_group)
            print(f"Added superuser to group '{ADMIN_GROUP}'")

        print("Done")
