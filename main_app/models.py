from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from datetime import date

# Create your models here.
SERVICES = (
    ('TU', 'Tune Up'),
    ('OC', 'Oil Change'),
)

class Car(models.Model):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    year = models.IntegerField()

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse("cars_detail", kwargs={"car_id": self.id})

    def serviced_this_month(self):
        return self.maintenance_set.filter(date=date.today()).count() >= len(SERVICES)

class Maintenance(models.Model):
    date = models.DateField('Maintenance Date')  
    service = models.CharField(
        max_length=2,
        choices=SERVICES,
        default=SERVICES[0][0]
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"
    
    # class Meta:
    #     ordering: ['-date']
class Gas(models.Model):
    gasType = models.CharField(max_length=50)

    def __str__(self):
        return self.gasType

    def get_absolute_url(self):
        return reverse("gas_detail", kwargs={"pk": self.id})
    
