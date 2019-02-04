from django_apscheduler.jobstores import register_job
from twilio.rest import Client
from .models import Appointment
from datetime import datetime
from .jobs import scheduler

# put your own credentials here
ACCOUNT_SID = "ACbb2e1d788c2f357359a6875f422e38fe"
AUTH_TOKEN = "2061c3f5e1388f8cec7cd5e02d9fa0e9"


def send_sms(receiver, sender, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to=receiver,
        from_=sender,
        body=message,
    )


@register_job(scheduler, "interval", seconds=5)
def remind_appointment_schedule():
    appointments = Appointment.objects.all()
    for appointment in appointments:
        print(appointment)
    print("==========================")
