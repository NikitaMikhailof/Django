from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive, name='index'),
]