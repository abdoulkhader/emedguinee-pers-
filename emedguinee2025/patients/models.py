from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_naissance = models.DateField(null=True, blank=True)
    sexe = models.CharField(max_length=10, choices=[('Homme', 'Homme'), ('Femme', 'Femme')])
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

from medecins.models import ProfilMedecin

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(ProfilMedecin, on_delete=models.CASCADE)
    date = models.DateField()
    motif = models.CharField(max_length=255)
    est_valide = models.BooleanField(default=False)

    def __str__(self):
        return f"RDV {self.patient} avec {self.medecin} le {self.date}"
