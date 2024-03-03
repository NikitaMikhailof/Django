from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Milk', discription='Milk is obtained from a cow',
        price=150.00, quantity=1)
        product.save()
        self.stdout.write(f'{product}')
