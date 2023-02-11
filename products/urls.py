from django.urls import path

from .views import categories, products

urlpatterns = [
    path('', categories, name='categories'),
    path('products/<int:category_id>/', products, name='products'),
    path('page/<int:category_id>/<int:page>/', products, name='paginator'),
]



