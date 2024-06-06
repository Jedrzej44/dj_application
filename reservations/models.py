from django.db import models

class Car(models.Model):

    CAR_COLORS_CHOICES = [("BLACK", "black"), ("WHITE", "white"), ("RED", "red"), ("GRAPHITE", "graphite")]
    CAR_TYPES = [("SUV", "SUV"), ("SPORT", "sport"), ("STANDARD", "standard")]
    color = models.CharField(choices=CAR_COLORS_CHOICES, max_length=16)
    car_types = models.CharField(choices=CAR_TYPES, max_length=16)
    model = models.CharField(max_length=100)
    seats = models.PositiveSmallIntegerField()
    price_per_day = models.DecimalField(decimal_places=2, max_digits=6)
    # horsepower =