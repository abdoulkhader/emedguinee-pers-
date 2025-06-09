from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfilMedecin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=100)
    numero_ordre = models.CharField(max_length=50)
    annees_experience = models.PositiveIntegerField()

    def __str__(self):
        return f"Dr {self.user.last_name} ({self.specialite})"
