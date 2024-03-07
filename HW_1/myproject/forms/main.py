from orders.models import User, Product, Order


def user_basket(user, product, quantity):
    list_product_in_order = []
    user = User.objects.filter(name=user).first()
    product = Product.objects.filter(name=product).first()
    list_product_in_order.append(product)

    if user and product is not None:
        order = Order(customer=user, quantity=quantity, total_price=(quantity * product.price))
        order.save()
        order.products.set(list_product_in_order)
        order.save() 
        return order.total_price
