from django.urls import path
from .views import user_form, user_profile, add_user, upload_image, order_user


urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('form/', user_profile, name='user_profile'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
    path('order/', order_user, name='order_user'),
]

