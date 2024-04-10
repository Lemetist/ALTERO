from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import index, home, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('adv/', include('shop.urls', namespace='products')),
    path('login/', include('users.urls')),
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
