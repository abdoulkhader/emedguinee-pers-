from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from users.models import CustomUser
from patients.models import Patient
from medecins.models import ProfilMedecin
from patients.models import RendezVous

def home_view(request):
    nb_patients = Patient.objects.count()
    nb_medecins = ProfilMedecin.objects.count()
    nb_rdv_valides = RendezVous.objects.filter(est_valide=True).count()

    context = {
        'nb_patients': nb_patients,
        'nb_medecins': nb_medecins,
        'nb_rdv_valides': nb_rdv_valides,
    }
    return render(request, 'core/home.html', context)

from django.shortcuts import render

def home_view(request):
    return render(request, 'core/home.html')  # assure-toi que ce fichier existe
