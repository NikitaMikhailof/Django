import logging
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UserForm, UserProfile, ImageForm, OrderForm
from .main import UserBasket
from .models import User


logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name} {email} {age}.')
    else:
        form = UserForm()

    return render(request, 'forms/user_form.html', {'form': form}) 


# def many_field_form(request):
#     if request.method == 'POST':
#         form = ManyFieldsFormWidget(request.POST)
#         if form.is_valid():
           
#             logger.info(f'Получили {form.cleaned_data=}.')
#     else:
#         form = ManyFieldsFormWidget()

#     return render(request, 'forms/many_field_form.html', {'form': form}) 


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'forms/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'forms/upload_image.html', {'form': form})


def order_user(request):
    if request.method  == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            user_basket = UserBasket()
            user_basket.send_the_order(user, product, quantity)

            context = {'user': user, 
                       'product': product,
                       'quantity': quantity,
                       'price': user_basket.total_price,
                        'time': user_basket.date_ordered}
            return render(request, 'forms/order.html', context) 
    else:
        form = OrderForm() 
    return render(request, 'forms/create_order.html', {'form': form})  


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'forms/upload_image.html', {'form': form})



def user_profile(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)
        form_upload_image = ImageForm(request.POST, request.FILES)

        if form_upload_image.is_valid():
            image = form_upload_image.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    
            context = {'form': UserProfile(),
                       'form_upload_image' : ImageForm(),
                        'message': 'Фото пользователя успешно обновлено'
                        }          
            
            return render(request, 'forms/user_profile.html', context) 

        if form.is_valid():
            name = form.cleaned_data['name']

            context = {'form': UserProfile(),
                       'form_upload_image' : ImageForm(),
                        'name': f'Пользователь {name} успешно обновил учетную запись'
                        }
            
            return render(request, 'forms/user_profile.html', context)
                
    else:
        form = UserProfile()
        form_upload_image = ImageForm()
        context = {'form': form, 'form_upload_image': form_upload_image}   

    return render(request, 'forms/user_profile.html', context) 