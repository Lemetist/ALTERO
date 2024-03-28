"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.hogme, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shop.views import index, profile, home, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('adv/', include('shop.urls', namespace='products') ),
    path('login/', include('users.urls', namespace='login')),
    path('profile/', profile, name='profile'),
    path('home/',home, name='home'),
    path('contacts/',contacts, name='contacts')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
