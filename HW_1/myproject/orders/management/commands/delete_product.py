from django.core.management.base import BaseCommand
from orders.models import Product

class Command(BaseCommand):
    help = "Delete product by name"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        product = Product.objects.filter(name=name).first()
        if product is not None:
            product.delete()
            self.stdout.write(f'{product}')

