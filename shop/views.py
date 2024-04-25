from django.shortcuts import render
from users.models import Advertisement

def index(request):
    return render(request, 'index.html')

def products(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement.html', {'advertisements': advertisements})

def contacts(request):
    return render(request, 'contacts.html')

def home(request):
    return index(request)
