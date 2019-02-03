from django.urls import path

from . import views

app_name = 'reminder'
urlpatterns = [
    path('appointments',
         views.AppointmentList.as_view(),
         name='AppointmentList'),
]
