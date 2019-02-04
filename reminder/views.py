from apscheduler.triggers.date import DateTrigger
from django.views.generic import ListView
from reminder.models import Appointment
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import AppointmentForm
from .jobs import scheduler
from .sms import remind_appointment_schedule
from datetime import timedelta, datetime


class AppointmentList(ListView):
    """
    Structures our Appointment data in a list view
    """
    model = Appointment


def create_appointment(request):
    """
    View function to handle our create appointment form
    :param request: Contains our request object
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppointmentForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()

            appointment = Appointment.objects.last()  # retrieve last saved appointment object

            # Calculate 30 less than scheduled date
            reminder = datetime.strptime(form.data['date'], '%m/%d/%Y %H:%M') - timedelta(minutes=30)

            # Configure our scheduler for reminder
            trigger = DateTrigger(
                run_date=reminder
            )
            scheduler.add_job(remind_appointment_schedule, args=[appointment], trigger=trigger)
            # redirect to a new URL:
            return redirect('/appointments')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AppointmentForm()

    return render(request, 'appointment_form.html', {'form': form})


def home(request):
    """View for our home page"""
    return render(request, 'home.html')
