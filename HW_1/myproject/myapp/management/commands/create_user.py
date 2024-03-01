from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Sergey', email='sboyk1992@mail.ru',
        telephone='89061390144', address='Kazan')
        user.save()
        self.stdout.write(f'{user}')

