from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='cars_index'),
  path('cars/<int:car_id>', views.cars_detail, name='cars_detail'),
  path('cars/create/', views.CarCreate.as_view(), name = 'cars_create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  path('cars/<int:car_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
  path('cara/<int:car_id>/assoc_gas/<int:gas_id>/', views.assoc_gas, name='assoc_gas'),
  path('gas/create/', views.GasCreate.as_view(), name='gas_create'),
  path('gas/<int:pk>/', views.GasDetail.as_view(), name='gas_detail'),
  path('gas/', views.GasList.as_view(), name='gas_index'),
  path('gas/<int:pk>/update/', views.GasUpdate.as_view(), name='gas_update'),
  path('gas/<int:pk>/delete/', views.GasDelete.as_view(), name='gas_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]