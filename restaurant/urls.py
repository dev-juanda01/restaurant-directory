from django.urls import path
from .views import list_restaurants, create_restaurant, search_restaurant

urlpatterns = [
    path('', list_restaurants, name='restaurants'),
    path('create/', create_restaurant, name='create_restaurant'),
    path('search/', search_restaurant, name='search_restaurant')
]
