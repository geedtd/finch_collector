from django.contrib import admin
from .models import Car, Maintenance, Gas

admin.site.register(Car)
admin.site.register(Maintenance)
admin.site.register(Gas)