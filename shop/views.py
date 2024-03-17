from django.shortcuts import render

def index(request):
    return render(request, 'index.html', )

def products(request):
    return render(request, 'advertisement.html')

def products_create(request):
    return  render(request, 'products.html')

def profile(request):
    return render(request, 'profile.html')


def contacts(request):
    return render(request, 'contacts.html')


def home(request):
    return index(request)