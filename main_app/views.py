# from _typeshed import HasFileno
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Gas, Maintenance
from .forms import MaintenanceForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Add the following import
# from django.http import HttpResponse



# Define the home view
# def home(request):
#   return HttpResponse('<h1>🚗  Vroom, vroom!</h1>')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

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

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

class Home(LoginView):
  template_name = 'home.html'

@login_required
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    gas_car_doesnt_have = Gas.objects.exclude(id__in = car.gas.all().values_list('id'))
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', { 
        'car': car, 'maintenance_form': maintenance_form, 'gas': gas_car_doesnt_have
    })


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['model','brand','description','year']
    # success_url = '/cars/'

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  # Let's disallow the renaming of a Car by excluding the name field!
  fields = ['model', 'description', 'year']

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'

@login_required
def add_maintenance(request, car_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.car_id = car_id
    new_maintenance.save()
  return redirect('cars_detail', car_id=car_id)


class GasCreate(LoginRequiredMixin, CreateView):
  model = Gas
  fields = '__all__'

class GasList(LoginRequiredMixin, ListView):
  model = Gas

class GasDetail(LoginRequiredMixin, DetailView):
  model = Gas

class GasUpdate(LoginRequiredMixin, UpdateView):
  model = Gas
  fields = ['gasType']

class GasDelete(LoginRequiredMixin, DeleteView):
  model = Gas
  success_url = '/gas/'

@login_required
def assoc_gas(request, car_id, gas_id):
  Car.objects.get(id = car_id).gas.add(gas_id)
  return redirect('cars_detail', car_id=car_id)