from django.core.management.base import BaseCommand
from orders.models import User

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Danil', email='danilak1992@mail.ru',
        telephone='89821323414', address='Samara')
        user.save()
        self.stdout.write(f'{user}')

