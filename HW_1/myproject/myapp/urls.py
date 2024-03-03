from django.urls import path
from .views import index, about, view_for, user_orders, user_orders_sort_time

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('for/', view_for, name='template_for'),
    path('user/<int:user_id>/', user_orders, name='user_orders'),
    path('sort_product/<int:user_id>/', user_orders_sort_time, name='user_orders'),
]