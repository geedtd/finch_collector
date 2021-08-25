from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Gas, Maintenance
from .forms import MaintenanceForm

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
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', { 
        'car': car, 'maintenance_form': maintenance_form
    })

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    # success_url = '/cars/'

class CarUpdate(UpdateView):
  model = Car
  # Let's disallow the renaming of a Car by excluding the name field!
  fields = ['model', 'description', 'year']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

def add_maintenance(request, car_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.car_id = car_id
    new_maintenance.save()
  return redirect('cars_detail', car_id=car_id)

class GasCreate(CreateView):
  model = Gas
  fields = __all__