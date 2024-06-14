from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from reservations.forms import ConfirmReservationForm
from reservations.models import Car, Client, Reservation

# Create your views here.
class HomeView(ListView):
    model = Car
    template_name = "home_view.html"
    context_object_name = "object_list"

class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"

def confirm_reservation(request, car_id):

    if request.method == "POST":
        form = ConfirmReservationForm(request.POST)
        if form.is_valid():
            client, created = Client.objects.get_or_create(email=form.cleaned_data["email"], defaults={"phone": form.cleaned_data["phone"], "birth_day": form.cleaned_data["birth_day"]})
            car = get_object_or_404(Car, id=car_id)
            if not Reservation.objects.filter(car=car).exists():
                reservation = Reservation.objects.create(client=client, car=car)
                print(f"Your reservation {reservation} has been created")
                return redirect("home_view")
            else:
                form = ConfirmReservationForm()

    else:
        form = ConfirmReservationForm()

    return render(request, "confirm_reservation.html", {"form": form, "car_id": car_id})

