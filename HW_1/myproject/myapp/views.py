import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect


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


def home(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Страница приложения пиццерии Modernissimo<h1>")



@log_user_visiting
def about(request):
    return HttpResponse(f"<h1>Наше заведение работает с 1999 года</h1>")



@log_user_visiting
def archive(request, year):
    if int(year) > 2024:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


