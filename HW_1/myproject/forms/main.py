from orders.models import User, Product, Order


class UserBasket():

    '''Create basket user'''

    def send_the_order(self, user_name, product_name, quantity):

        list_product_in_order = []

        user = User.objects.filter(name__iexact=user_name).first()
        product = Product.objects.filter(name__iexact=product_name).first() 
        list_product_in_order.append(product)

        order = Order(customer=user, quantity=quantity, total_price=quantity * product.price)
        order.save()
        self.total_price = order.total_price 
        self.date_ordered = order.date_ordered
        order.products.set(list_product_in_order)
        order.save()
        
    