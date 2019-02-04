from django.db import models
from django.utils import timezone
from .jobs import scheduler


class Appointment(models.Model):
    """Appointment schema"""
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    date = models.DateTimeField()
    tel = models.IntegerField(default=None)

    def __str__(self):
        return "{} {}".format(self.content, self.date)


scheduler.start()
