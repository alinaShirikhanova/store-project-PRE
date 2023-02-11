from django.urls import path
from users.views import auth_user, register

urlpatterns = [
    path('authorization/', auth_user, name='auth'),
    path('registration/', register, name='register'),
]
