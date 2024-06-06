#admin - admin@admin.com - admin

from django.contrib import admin

from reservations.models import Car

class CarAdmin(admin.ModelAdmin):
    fields = ["car_types", "model", "horsepower", "seats", "price_per_day", "color"]
    list_display = ["car_types", "model", "horsepower", "seats", "price_per_day", "color"]


admin.site.register(Car, CarAdmin)


