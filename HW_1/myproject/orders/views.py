import logging
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Order, Product


logger = logging.getLogger(__name__)


'''декоратор для логгированния запуска функций'''
def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        res = str(*result)[-9:-5]
        logger.info(f'Была запущена функция {func.__name__} которая вернула {res}')
        return result
    return wrapper


'''декоратор для логгированния посещений страниц пользователем'''
def log_user_visiting(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Пользователь посетил страницу {func.__name__}')
        return result
    return wrapper


def user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user).order_by('-date_ordered')
    dict_products_in_order = dict()

    for order in orders:
        lst_products = []
        for product in order.products.filter(order=order):
           lst_products.append(product)
        dict_products_in_order[order.date_ordered] = lst_products
        
    context = {'user': user, 'orders': orders, 'dict_products_in_order': dict_products_in_order}
    return render(request, 'orders/user_orders.html', context)
    


def user_orders_sort_time(request, user_id):

    from datetime import datetime

    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user)
    set_week, set_month, set_year = set(), set(), set()
    today = datetime.now()

    for order in orders:
        delta = (today - datetime.fromisoformat(str(order.date_ordered)[:10])).days
        if delta <= 7:
            for product in order.products.all():
                set_week.add(product.name)
                set_month.add(product.name)
                set_year.add(product.name)
        elif delta <= 30:
            for product in order.products.all():
                set_month.add(product.name)
                set_year.add(product.name)
        elif delta <= 365:
            for product in order.products.all():
                set_year.add(product.name)

    context = {
        "user": user,
        "set_week": set_week,
        "set_month": set_month,
        "set_year": set_year,
    }

    return render(request, "orders/user_products_sort_time.html", context)
   


  



