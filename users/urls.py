from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import *

urlpatterns = [
    path('authorization/', UserLoginView.as_view(), name='auth'),
    path('registration/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
