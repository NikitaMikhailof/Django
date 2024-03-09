from django.core.management.base import BaseCommand
from orders.models import User, Product, Order

class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('name_user', type=str, help='User name')
        parser.add_argument('name_product', type=str, help='Product name')
        parser.add_argument('quantity_product', type=int, help='Product quantity')

    def handle(self, *args, **kwargs):
        name_user = kwargs.get('name_user')
        name_product = kwargs.get('name_product')
        quantity_product = kwargs.get('quantity_product')

        list_product_in_order = []
        user = User.objects.filter(name=name_user).first()
        product = Product.objects.filter(name=name_product).first()
        list_product_in_order.append(product)

        if user and product is not None:
            order = Order(customer=user, quantity=quantity_product, total_price=(quantity_product * product.price))
            order.save()
            order.products.set(list_product_in_order)
            order.save()

            self.stdout.write(f'{order}')