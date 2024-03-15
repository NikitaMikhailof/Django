from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Главная страница сайта заказа товаров")


def about(request):
    return HttpResponse("О нас")
