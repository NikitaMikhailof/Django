from django.core.management.base import BaseCommand
from orders.models import Product

class Command(BaseCommand):
    help = "Get all products"

    def handle(self, *args, **kwargs):
        product = Product.objects.all()
        self.stdout.write(f'{product}')