from django.core.management.base import BaseCommand
from orders.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Bread', discription='bread is made from flour', price=50.00)
        product.save()
        self.stdout.write(f'{product}')

 