from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant
# Create your views here.

def create(request):
    #creacion de los elementos
    place = Place(name="lugar 1", address="calle demo")
    place.save()

    restaurant = Restaurant(place=place, number_of_employees=8)
    restaurant.save()

    return HttpResponse(restaurant.place.name)
