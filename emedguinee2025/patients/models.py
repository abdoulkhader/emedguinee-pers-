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


class DossierMedical(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name="dossier")

    # Informations administratives
    numero_dossier = models.CharField(max_length=50, blank=True, null=True)
    medecin_referent = models.ForeignKey('medecins.ProfilMedecin', null=True, blank=True, on_delete=models.SET_NULL)
    date_creation = models.DateField(auto_now_add=True)

    # Allergies
    allergie_medicament = models.TextField(blank=True, null=True)
    allergie_alimentaire = models.TextField(blank=True, null=True)
    allergie_autre = models.TextField(blank=True, null=True)

    # Antécédents
    maladies_chroniques = models.TextField(blank=True, null=True)
    chirurgies = models.TextField(blank=True, null=True)

    # Traitements en cours
    traitement_medicament = models.TextField(blank=True, null=True)
    traitement_posologie = models.TextField(blank=True, null=True)

    # Vaccinations
    vaccin_covid = models.CharField(max_length=50, blank=True, null=True)
    vaccin_hepatite_b = models.CharField(max_length=50, blank=True, null=True)

    # Groupe sanguin
    groupe_sanguin = models.CharField(max_length=3, blank=True, null=True)
    rhesus = models.CharField(max_length=10, blank=True, null=True)

    # Constantes vitales
    tension_arterielle = models.CharField(max_length=20, blank=True, null=True)
    frequence_cardiaque = models.CharField(max_length=20, blank=True, null=True)
    temperature = models.CharField(max_length=20, blank=True, null=True)
    poids = models.CharField(max_length=10, blank=True, null=True)

    # Contact d'urgence
    contact_urgence_nom = models.CharField(max_length=100, blank=True, null=True)
    contact_urgence_telephone = models.CharField(max_length=20, blank=True, null=True)
    contact_urgence_lien = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Dossier de {self.patient.user.get_full_name()}"


from django.db import models
from django.contrib.auth import get_user_model
from medecins.models import ProfilMedecin

User = get_user_model()

class MessagePatient(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    medecin = models.ForeignKey(ProfilMedecin, on_delete=models.CASCADE)
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.patient} à {self.medecin} le {self.date_envoi.strftime('%d/%m/%Y')}"
    

class Consultation(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    medecin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    motif = models.CharField(max_length=255)
    notes = models.TextField()

    def __str__(self):
        return f"Consultation du {self.date} - {self.patient.user.get_full_name()}"
