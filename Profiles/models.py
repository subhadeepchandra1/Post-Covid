from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta
<<<<<<< HEAD
from django.core.files.storage import FileSystemStorage
from django.conf import settings
=======
>>>>>>> 1bff0b3c851709a031faa42116d7f8afb8d6269b

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
<<<<<<< HEAD
    social_active = models.BooleanField(default=False)
    social_count = models.IntegerField(default=0)
    #social_video =models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), 
    #upload_to='logos', default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    social_image =models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), 
    upload_to='logos', default='settings.MEDIA_ROOT/logos/anonymous.jpg')
=======
>>>>>>> 1bff0b3c851709a031faa42116d7f8afb8d6269b

    def send_notification(self):
        now = timezone.now()
        if now - self.timer_last_active >= td:
           self.save()  # Updates current execution time
           return True
        return False