from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta

# specifying choices 
CHOICES = ( 
    ("Manager", "Manager"), 
    ("Employee", "Regular Employee"),
) 

class CustomUser(AbstractUser):
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    employment = models.CharField( max_length = 20, choices = CHOICES, default = "Manager")
    timer_active = models.BooleanField(default=False)
    timer_last_active = models.DateTimeField(default=datetime.now())

    def send_notification(self):
        now = timezone.now()
        if now - self.timer_last_active >= td:
           self.save()  # Updates current execution time
           return True
        return False