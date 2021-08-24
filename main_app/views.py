from django.shortcuts import render
from .models import Car

# Add the following import
# from django.http import HttpResponse



# Define the home view
# def home(request):
#   return HttpResponse('<h1>🚗  Vroom, vroom!</h1>')

def about(request):
  return render(request, 'about.html')

# class Car:
#     def __init__(self, model, brand, description, year):
#         self.model = model
#         self.brand = brand
#         self.description = description
#         self.year = year

# cars = [
#     Car('Mustang', 'Ford', '289 V8', 1965)
# ]

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def home(request):
  return render(request, 'home.html')   

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', { 'car': car})