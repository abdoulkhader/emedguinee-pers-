from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient, RendezVous
from .forms import PriseRendezVousForm
from medecins.models import ProfilMedecin
from django.utils.timezone import now


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
    patient = get_object_or_404(Patient, user=request.user)
    dossier = getattr(patient, 'dossier', None)  # lié par OneToOneField

    return render(request, 'patients/dossier_medical.html', {
        'user': request.user,
        'patient': patient,
        'dossier': dossier,
    })

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


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Patient, DossierMedical

@login_required
def telecharger_dossier(request):
    # Vérifie que l'utilisateur est un patient
    patient = get_object_or_404(Patient, user=request.user)
    dossier = getattr(patient, 'dossier', None)

    # Charge le template HTML du PDF
    template_path = 'patients/dossier_pdf.html'
    context = {
        'patient': patient,
        'dossier': dossier,
        'current_date': now(),
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mon_dossier_medical.pdf"'

    # Génère le PDF
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Si erreur dans la génération
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF', status=500)

    return response



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactMedecinForm
from .models import Patient

@login_required
def contacter_medecin(request):
    patient = Patient.objects.get(user=request.user)

    if request.method == 'POST':
        form = ContactMedecinForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.patient = patient
            message.save()
            return redirect('patient_dashboard')  # ou page de confirmation
    else:
        form = ContactMedecinForm()

    return render(request, 'patients/contacter_medecin.html', {'form': form})


from .models import Patient, Consultation

@login_required
def historique_consultations(request):
    patient = get_object_or_404(Patient, user=request.user)
    consultations = Consultation.objects.filter(patient=patient).order_by('-date')
    return render(request, 'patients/historique_consultations.html', {
        'patient': patient,
        'consultations': consultations,
    })