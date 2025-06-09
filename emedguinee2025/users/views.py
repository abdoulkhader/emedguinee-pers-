from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterPatientForm, RegisterMedecinForm

def register_patient(request):
    if request.method == 'POST':
        form = RegisterPatientForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = RegisterPatientForm()
    return render(request, 'users/register_patient.html', {'form': form})


def register_medecin(request):
    if request.method == 'POST':
        form = RegisterMedecinForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('medecin_dashboard')
    else:
        form = RegisterMedecinForm()
    return render(request, 'users/register_medecin.html', {'form': form})

def choix_inscription(request):
    if request.method == 'GET' and 'role' in request.GET:
        role = request.GET.get('role')
        if role == 'patient':
            return redirect('register_patient')
        elif role == 'medecin':
            return redirect('register_medecin')
    return render(request, 'users/choix_inscription.html')
from django.shortcuts import render
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'users/login.html'  # ton propre template

from django.shortcuts import redirect

def redirect_after_login(request):
    user = request.user
    if user.is_superuser or user.is_admin:
        return redirect('admin_dashboard')  # à adapter si admin a un dashboard
    elif user.is_medecin:
        return redirect('medecin_dashboard')
    elif user.is_patient:
        return redirect('patient_dashboard')
    else:
        return redirect('home')  # par défaut
