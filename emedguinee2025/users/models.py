from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_medecin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)  # facultatif s