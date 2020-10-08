from django.contrib.auth.models import AbstractUser
from django.db import models

# specifying choices 
  
CHOICES = ( 
    ("Manager", "Manager"), 
    ("Employee", "Regular Employee"),
) 

class CustomUser(AbstractUser):
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    employment = models.CharField( max_length = 20, choices = CHOICES, default = "Manager") 