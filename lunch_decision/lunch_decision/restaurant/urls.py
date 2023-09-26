from django.urls import path
from .views import create_restaurant, restaurant_authentication

urlpatterns = [
    path('create/', create_restaurant, name='create-restaurant'),
    path('authenticate/', restaurant_authentication, name='restaurant-authentication'),
]
