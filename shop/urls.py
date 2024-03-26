
from django.urls import path
from shop.views import products

app_name = 'myshop'

urlpatterns = [
    path('', products, name='index')

]

