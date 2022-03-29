from django.db import models
from django.contrib.auth.models import User
from locations import models as location
from vendors import models as vendors

# Create your models here.
class Profile(models.Model):
    # relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(location.Country, on_delete=models.CASCADE)
    city = models.ForeignKey(location.City, on_delete=models.CASCADE)
    # fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    credit = models.IntegerField()

    def __str__(self):
        return self.first_name


class Cart(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(vendors.Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(
        vendors.Product,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="cart_product",
    )

    # fields
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    # def __str__(self):
    #     return self.user.username
