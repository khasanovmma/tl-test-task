import random

from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import DynamicProvider

from structure.models import Employee


def get_professions():
    with open('professions.txt', 'r') as file:
        return file.read().split("\n")


def add_employees(number, self):
    professions_provider = DynamicProvider(
        provider_name='professions_provider',
        elements=get_professions()
    )

    for _ in range(number//2000):
        fake = Faker()
        fake.add_provider(professions_provider)
        
        Employee.objects.create(
                full_name=fake.name(),
                position=fake.professions_provider(),
                employment_date=fake.date_between(start_date='-10y', end_date='today'),
                salary=5000,
            )

        for _ in range(1999):
            Employee.objects.create(
                full_name=fake.name(),
                position=fake.professions_provider(),
                employment_date=fake.date_between(start_date='-10y', end_date='today'),
                salary=random.randrange(500, 5000),
                parent=Employee.objects.filter(level__lt=5).order_by('?').first()
            )
    print(f"{number} employees successfully created")       
    return number


class Command(BaseCommand):
    help = 'Generates test data for Employees'

    def add_arguments(self, parser):
        parser.add_argument(
            'n_emp',
            nargs='?',
            type=int,
            help='The number of employees',
            default=100
        )

    def handle(self, *args, **options):
        Employee.objects.all().delete()
        count_employees = add_employees(options['n_emp'], self)