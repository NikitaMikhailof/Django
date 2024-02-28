from django.db import models


class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True) 
    is_active = models.BooleanField(default=True)



