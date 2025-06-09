from django.shortcuts import render

# Create your views here.
from django.db import models

class Etablissement(models.Model):
    nom = models.CharField(max_length=100, default='e_medGuinée')
    email_contact = models.EmailField()
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nom
