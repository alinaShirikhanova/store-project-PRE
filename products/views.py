from django.shortcuts import render

from products.models import Category


def index(request):
    return render(request, 'products/index.html')

def categories(request):
    context = {
        'categories':Category.objects.all(),
    }
    return render(request, 'products/categories.html', context)
