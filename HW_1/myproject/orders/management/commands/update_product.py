from django.core.management.base import BaseCommand
from orders.models import Product

class Command(BaseCommand):
    help = "Update product by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.save()
        self.stdout.write(f'{product}')

