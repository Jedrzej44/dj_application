#admin - admin@admin.com - admin

from django.contrib import admin

from reservations.models import Car, Client, Reservation

class CarAdmin(admin.ModelAdmin):
    fields = ["id", "car_type", "model", "horsepower", "seats", "price_per_day", "color"]
    list_display = ["id", "car_type", "model", "horsepower", "seats", "price_per_day", "color"]
    readonly_fields = ["id"]

class ClientAdmin(admin.ModelAdmin):
    fields = ["email", "phone", "birth_day"]
    list_display = ["email", "phone", "birth_day"]

class ReservationAdmin(admin.ModelAdmin):
    fields = ["id", "date_of_creation", "client", "car", "reservation_days", "total_price"]
    list_display = ["id", "date_of_creation", "client", "car", "reservation_days", "total_price"]
    readonly_fields = ["date_of_creation", "total_price", "id"]

admin.site.register(Car, CarAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Reservation, ReservationAdmin)

