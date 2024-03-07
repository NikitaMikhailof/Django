from django.urls import path
from .views import user_form, many_field_form, add_user, upload_image, order_user


urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('form/', many_field_form, name='many_field_form'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
    path('order/', order_user, name='order_user'),
]

