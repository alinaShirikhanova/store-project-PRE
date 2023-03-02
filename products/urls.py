from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    path('', CategoriesListView.as_view(), name='categories'),
    path('products/<int:category_id>/', cache_page(120)(ProductsListView.as_view()), name='products'),
    path('page/<int:category_id>/<int:page>/',cache_page(120)(ProductsListView.as_view()), name='paginator'),
    path('page/<int:page>/', CategoriesListView.as_view(), name='category_paginator'),
    path('basket/', basket, name='basket'),
    path('basket/add/<int:product_id>/', add_product, name='add_product'),
    path('basket/delete/<int:basket_id>/', delete_product, name='delete_product'),
    path('basket/remove/<int:product_id>/', remove_product, name='remove_product'),
]



