from django.shortcuts import render

from shop.models import Product


def index(request):
    return render(request, 'index.html', )

def products(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'advertisement.html',context)

def products_create(request):
    context ={
        'tower': Product.objects.all()
    }
    return  render(request, 'products.html', context)

def profile(request):
    return render(request, 'profile.html')


def contacts(request):
    return render(request, 'contacts.html')


def home(request):
    return index(request)