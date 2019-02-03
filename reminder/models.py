from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    """Appointment schema"""
    content = models.TextField(default="")
    date = models.DateTimeField(default=timezone.now())
    tel = models.IntegerField(default=None)

    def __str__(self):
        return "{} {}".format(self.content, self.date)
