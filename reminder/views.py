from django.shortcuts import render
from django.views.generic import ListView
from reminder.models import Appointment


class AppointmentList(ListView):
    model = Appointment
