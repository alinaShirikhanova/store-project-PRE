from django.urls import path
from users.views import auth_user, register, profile, logout

urlpatterns = [
    path('authorization/', auth_user, name='auth'),
    path('registration/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
