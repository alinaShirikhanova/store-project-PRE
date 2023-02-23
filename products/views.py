from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from products.models import Category, Product, Basket


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


@login_required
def basket(request):
    user_basket = Basket.objects.all()
    context = {'baskets': user_basket}
    return render(request, 'products/basket.html', context)


@login_required
def add_product(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        baskets = baskets.last()
        baskets.quantity += 1
        baskets.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def delete_product(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
