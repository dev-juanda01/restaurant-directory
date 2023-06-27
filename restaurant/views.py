from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.


def list_restaurants(request):
    restaurants = Restaurant.objects.all()

    return render(request, 'index.html', {
        'restaurants': restaurants
    })


def create_restaurant(request):
    if request.method == "GET":
        restaurant_form = RestaurantForm()
        return render(request, 'new_restaurant.html', {
            'restaurant_form': restaurant_form
        })
    else:
        restaurant_form = RestaurantForm(request.POST)

        if restaurant_form.is_valid():
            restaurant_form.save()
            return redirect('restaurant:restaurants')


def search_restaurant(request):
    restaurant = None

    if request.method == "GET":
        return render(request, 'search_restaurant.html', {
            'restaurant': 1
        })
    else:
        name = request.POST['restaurant']
        restaurant = Restaurant.objects.filter(name=name).first()

        if restaurant:
            return render(request, 'search_restaurant.html', {
                'restaurant': restaurant
            })

        return render(request, 'search_restaurant.html', {
            'restaurant': restaurant
        })
