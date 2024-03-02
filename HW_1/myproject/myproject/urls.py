"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import index, about, view_for, user_orders, user_orders_sort_time
from myproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('for/', view_for),
    path('user/<int:user_id>/', user_orders, name='user_orders'),
    path('sort_product/<int:user_id>/', user_orders_sort_time, name='user_orders_sort_time'),
]

if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
