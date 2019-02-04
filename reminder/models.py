from django.db import models
from .jobs import scheduler


class Appointment(models.Model):
    """Appointment schema"""
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    date = models.DateTimeField()
    tel = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.content, self.date)


# Start our scheduler
scheduler.start()
