from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from products.models import Category, Product, Basket
from users.models import User


class MainView(TemplateView):
    template_name = 'products/index.html'


# def index(request):
#     return render(request, 'products/index.html')

class CategoriesListView(ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    paginate_by = 3



def categories(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'products/categories.html', context)


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 1


    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        return queryset.filter(category=category)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


# def products(request, category_id, page=1):
#     category = Category.objects.get(id=category_id)
#     products_by_category = Product.objects.filter(category=category)
#     per_page = 1
#     paginator = Paginator(products_by_category, per_page)
#     products_paginator = paginator.page(page)
#
#     context = {'products': products_paginator, 'category': category}
#     return render(request, 'products/products.html', context)



@login_required
def basket(request):
    user_basket = Basket.objects.filter(user=request.user)
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


def remove_product(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    baskets = baskets.last()
    if baskets.quantity > 1:
        baskets.quantity -= 1
        baskets.save()
    else:
        baskets.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def delete_product(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
