from django.core.paginator import Paginator
from django.shortcuts import render

from products.models import Category, Product


def index(request):
    return render(request, 'products/index.html')


def categories(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'products/categories.html', context)


def products(request, category_id, page=1):
    category = Category.objects.get(id=category_id)
    products_by_category = Product.objects.filter(category=category)
    per_page = 1
    paginator = Paginator(products_by_category, per_page)
    products_paginator = paginator.page(page)

    context = {'products': products_paginator, 'category': category}
    return render(request, 'products/products.html', context)
