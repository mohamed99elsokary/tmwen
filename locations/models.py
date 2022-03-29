from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
