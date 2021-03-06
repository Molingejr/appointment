from django.urls import path
from . import views

"""Register our all url paths for our app"""

app_name = 'reminder'
urlpatterns = [
    path('', views.home, name='home'),
    path('appointments',
         views.AppointmentList.as_view(),
         name='AppointmentList'),
    path(r'create_appointments', views.create_appointment, name='create_appointment'),
]
