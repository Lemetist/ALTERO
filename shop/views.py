from django.shortcuts import render

def index(request):
    context = {
        'title' : 'test title',
        'username' : 'test username',
    }

    return render(request, 'index.html', context)


def products(request):
    return  render(request, 'products.html')
