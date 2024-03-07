from django.urls import path
from .views import  user_orders, user_orders_sort_time

urlpatterns = [
    path('user/<int:user_id>/', user_orders, name='user_orders'),
    path('sort_product/<int:user_id>/', user_orders_sort_time, name='user_orders'),
]