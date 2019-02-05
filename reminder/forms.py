from django import forms
from django.forms import ModelForm
from .models import Appointment


class AppointmentForm(ModelForm):
    """Appointment form which uses our Appointment model"""
    class Meta:
        model = Appointment
        fields = ['title', 'content', 'date', 'tel']
        widgets = {
            'date': forms.DateTimeInput(attrs={'id': 'input', 'style': "text-align: center"})
        }
