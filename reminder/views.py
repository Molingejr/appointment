from django.views.generic import ListView
from reminder.models import Appointment
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import AppointmentForm
from .sms import hello


class AppointmentList(ListView):
    model = Appointment


def create_appointment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppointmentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect('/appointments')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AppointmentForm()

    return render(request, 'appointment_form.html', {'form': form})


def home(request):
    return render(request, 'home.html')
