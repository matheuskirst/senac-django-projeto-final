from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from ...models import EmployeeProfile
from ...groups import ADMINISTRATOR_GROUP, OPERATOR_GROUP

class Command(BaseCommand):
    help = "Populate the database with employees"

    def handle(self, *args, **options):
        self.create_admins()
        self.create_operators()

    def create_admins(self):
        User = get_user_model()

        user = User.objects.create_user(
            username='administrador',
            password='Teste12345',
            is_employee=True
        )

        user.groups.add(Group.objects.get(name=ADMINISTRATOR_GROUP))

        EmployeeProfile.objects.create(
            first_name="John",
            last_name="Marston",
            cpf="32145666512",
            date_of_birth="2000-01-02",
            user=user
        )

    def create_operators(self):
        User = get_user_model()

        users = [
            ("12345678901", "João", "Silva"),
            ("23456789012", "Maria", "Santos"),
            ("34567890123", "Pedro", "Oliveira"),
            ("45678901234", "Ana", "Costa"),
            ("56789012345", "Lucas", "Pereira"),
            ("67890123456", "Juliana", "Ferreira"),
            ("78901234567", "Gabriel", "Rodrigues"),
            ("89012345678", "Camila", "Almeida"),
            ("90123456789", "Rafael", "Martins"),
            ("01234567890", "Beatriz", "Lima"),
        ]

        

        for cpf, first_name, last_name in users:
            user = User.objects.create_user(
                username=cpf,
                password="Teste12345",
                is_employee=True
            )

            user.groups.add(Group.objects.get(name=OPERATOR_GROUP))

            EmployeeProfile.objects.create(
                first_name=first_name,
                last_name=last_name,
                cpf=cpf,
                date_of_birth="2000-01-02",
                user=user
            )
