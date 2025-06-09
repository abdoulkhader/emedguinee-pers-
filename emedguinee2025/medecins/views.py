from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ProfilMedecin

@login_required
def dashboard_medecin(request):
    medecin = ProfilMedecin.objects.get(user=request.user)
    return render(request, 'medecins/dashboard_medecin.html', {'medecin': medecin})

from django.shortcuts import render
from .models import ProfilMedecin  # adapte si ton modèle s'appelle autrement

def liste_medecins(request):
    medecins = ProfilMedecin.objects.all()  # récupère tous les médecins
    return render(request, 'medecins/liste_medecins.html', {'medecins': medecins})