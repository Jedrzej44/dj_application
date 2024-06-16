from django.db import models
from datetime import date
from django.utils import timezone

class Car(models.Model):

    CAR_COLORS_CHOICES = [("BLACK", "black"), ("WHITE", "white"), ("RED", "red"), ("GRAPHITE", "graphite")]
    CAR_TYPES = [("SUV", "SUV"), ("SPORT", "sport"), ("STANDARD", "standard")]
    car_type = models.CharField(choices=CAR_TYPES, max_length=16)
    model = models.CharField(max_length=100)
    horsepower = models.DecimalField(decimal_places=0, max_digits=3, null=True)
    seats = models.PositiveSmallIntegerField()
    price_per_day = models.DecimalField(decimal_places=2, max_digits=6)
    color = models.CharField(choices=CAR_COLORS_CHOICES, max_length=16)

    def __str__(self):
        return f"{self.id}/{self.car_type}/{self.model}/{self.color}/{self.price_per_day}"

    #dlaczego to jest w rezerwacji??


class Client(models.Model):

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16)
    birth_day = models.DateField()

    def __str__(self):
        return f"{self.id}/{self.email}"

class Reservation(models.Model):
    date_of_creation = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name ="reservations")
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    reservation_days = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, editable=False)

    def __str__(self):
        return f"{self.client.email}/{self.car.model}"


    def save(self, *args, **kwargs):
        self.reservation_days = (self.end_date - self.start_date).days + 1
        self.total_price = self.car.price_per_day * self.reservation_days
        super(Reservation, self).save(*args, **kwargs)