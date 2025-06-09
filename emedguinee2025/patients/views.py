from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient, RendezVous
from .forms import PriseRendezVousForm
from medecins.models import ProfilMedecin

# 🟦 1. Tableau de bord patient
@login_required
def dashboard_patient(request):
    patient = get_object_or_404(Patient, user=request.user)
    rendez_vous = RendezVous.objects.filter(patient=patient).order_by('-date')
    medecins = ProfilMedecin.objects.all()
    return render(request, 'patients/patient_dashboard.html', {
        'patient': patient,
        'rendez_vous': rendez_vous,
        'medecins': medecins,
        'derniere_consultation': rendez_vous.first() if rendez_vous.exists() else None,
    })

# 🟦 2. Prise de rendez-vous (formulaire)
@login_required
def prendre_rdv_patient(request):
    patient = get_object_or_404(Patient, user=request.user)
    if request.method == 'POST':
        form = PriseRendezVousForm(request.POST)
        if form.is_valid():
            rdv = form.save(commit=False)
            rdv.patient = patient
            rdv.save()
            return redirect('patient_dashboard')
    else:
        form = PriseRendezVousForm()
    return render(request, 'patients/prise_rdv.html', {'form': form})


# 🟦 3. Mon profil
@login_required
def profil_patient(request):
    patient = get_object_or_404(Patient, user=request.user)
    return render(request, 'patients/profil_patient.html', {'patient': patient})


# 🟦 4. Mes rendez-vous
@login_required
def mes_rendez_vous(request):
    patient = get_object_or_404(Patient, user=request.user)
    rendez_vous = RendezVous.objects.filter(patient=patient)
    return render(request, 'patients/mes_rendez_vous.html', {
        'rendez_vous': rendez_vous,
    })


# 🟦 5. Mon dossier médical
@login_required
def dossier_medical(request):
    # À compléter avec les vraies données médicales plus tard
    return render(request, 'patients/dossier_medical.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ModifierProfilPatientForm
from .models import Patient

from django.contrib import messages  # 🔵 à importer

@login_required
def modifier_profil_patient(request):
    patient = get_object_or_404(Patient, user=request.user)

    if request.method == 'POST':
        form = ModifierProfilPatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Votre profil a bien été mis à jour.")
            return redirect('profil_patient')
    else:
        form = ModifierProfilPatientForm(instance=patient)

    return render(request, 'patients/modifier_profil_patient.html', {
        'form': form,
        'patient': patient
    })
