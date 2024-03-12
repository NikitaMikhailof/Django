from django.contrib import admin
from .models import  User, Order, Product


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'telephone', 'address', 'created_at']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'quantity', 'total_price', 'date_ordered']
    ordering = ['-date_ordered']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription', 'price', 'created_at']    


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
