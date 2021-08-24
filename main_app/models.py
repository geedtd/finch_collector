from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    year = models.IntegerField()

    def __str__(self):
        return self.model