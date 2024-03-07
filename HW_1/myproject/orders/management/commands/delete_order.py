from django.core.management.base import BaseCommand
from orders.models import Order

class Command(BaseCommand):
    help = "Delete order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        order.delete()
        self.stdout.write(f'Order id: {pk} is delete')


        
