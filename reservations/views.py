from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from reservations.forms import ConfirmReservationForm, CarFilterForm
from reservations.models import Car, Client, Reservation
from django.db.models import Q, Count


def filter_choice_field(qs, field, field_value):
    if field_value != "None":
        qs = qs.filter(**{field: field_value})
    return qs

def filter_non_required_field(qs, field, field_value):
    if field_value is not None:
        qs = qs.filter(**{field: field_value})
    return qs

class HomeView(ListView):
    model = Car
    template_name = "home_view.html"
    context_object_name = "object_list"


    def get_queryset(self):
        qs = Car.objects.annotate(num_reservations=Count("reservations")).filter(num_reservations=0)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CarFilterForm()
        return context

    def post(self, request, *args, **kwargs):
        qs = self.get_queryset()
        filter_form = CarFilterForm(request.POST)
        if filter_form.is_valid():
            car_type = filter_form.cleaned_data["car_type"]
            color = filter_form.cleaned_data["color"]
            seats = filter_form.cleaned_data["seats"]
            min_price = filter_form.cleaned_data["min_price"]
            max_price = filter_form.cleaned_data["max_price"]
            #price_per_day = filter_form.cleaned_data["price_per_day"]

            qs = filter_choice_field(qs, field="car_type", field_value=car_type)
            qs = filter_choice_field(qs, field="color", field_value=color)
            qs = filter_non_required_field(qs, field="seats", field_value=seats)
            #qs = filter_non_required_field(qs, field="price_per_day", field_value=price_per_day)

            if min_price is not None and max_price is not None:
                qs = qs.filter(price_per_day__gte=min_price, price_per_day__lte=max_price)
            elif min_price is not None:
                qs = qs.filter(price_per_day__gte=min_price)
            elif max_price is not None:
                qs = qs.filter(price_per_day__lte=max_price)

        context = {self.context_object_name: qs, "form": filter_form}
        return render(request, self.template_name, context)

class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"

def confirm_reservation(request, car_id):
    message1 = ""
    message2 = ""
    if request.method == "POST":
        form = ConfirmReservationForm(request.POST)
        if form.is_valid():
            client, created = Client.objects.get_or_create(
                email=form.cleaned_data["email"],
                defaults={
                    "phone": form.cleaned_data["phone"],
                    "birth_day": form.cleaned_data["birth_day"]
                }
            )
            car = get_object_or_404(Car, id=car_id)


            if not car.reservations.exists():
                reservation = Reservation.objects.create(client=client, car=car)
                message1 = "Reservation accepted!"
                message2 = (f"Your reservation number is: {reservation.id}")
                # return redirect("home_view")
            else:
                form = ConfirmReservationForm()
                message1 = "This car is already reserved!"
                message2 = "Please go to home view and select another car"
    else:
        form = ConfirmReservationForm()

    return render(request, "confirm_reservation.html", {
        "form": form,
        "car_id": car_id,
        "message1": message1,
        "message2": message2})

