from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from locations import models as locations

# Create your models here.
class Vendor(models.Model):
    # relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(
        locations.Country, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    city = models.ForeignKey(
        locations.City, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    # fields
    name = models.CharField(max_length=50)
    LAT = models.CharField(max_length=50)
    LONG = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    open_time = models.TimeField(auto_now=False, auto_now_add=False)
    close_time = models.TimeField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.name


class Product(models.Model):
    # relations
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    # fields
    image = models.ImageField(upload_to="media/")
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
