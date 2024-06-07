from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView

from reservations.models import Car, Client, Reservation

# Create your views here.
class CarListView(ListView):
    model = Car
    template_name = "home.html"
    context_object_name = "object_list"