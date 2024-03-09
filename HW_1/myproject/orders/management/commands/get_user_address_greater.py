from django.core.management.base import BaseCommand
from orders.models import User

class Command(BaseCommand):
    help = "Get user with age greater <address>."
    
    def add_arguments(self, parser):
        parser.add_argument('address', type=str, help='User email')

    def handle(self, *args, **kwargs):
        address = kwargs['address']
        user = User.objects.filter(address__iexact=address)
        self.stdout.write(f'{user}')
