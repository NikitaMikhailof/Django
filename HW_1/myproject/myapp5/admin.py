from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'category', 'quantity']


"""Отдельный продукт."""
# fields = ['name', 'description', 'category', 'date_added',
# 'rating']
readonly_fields = ['date_added', 'rating']
fieldsets = [
    (
        None,
        {
            'classes': ['wide'],
            'fields': ['name'],
        },
    ),
    (
        'Подробности',
        {   
            'classes': ['collapse'],
            'description': 'Категория товара и его подробное описание',
            'fields': ['category', 'description'],
        },
    ),
    (
        'Бухгалтерия',
        {
            'fields': ['price', 'quantity'], 
        }
    ),
    (
        'Рейтинг и прочее',
        {
            'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
            'fields': ['rating', 'date_added'],
        }
    ),
]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)


