from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from patients.models import Patient
from medecins.models import ProfilMedecin

class RegisterPatientForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            Patient.objects.create(user=user)
        return user


class RegisterMedecinForm(UserCreationForm):
    specialite = forms.CharField()
    numero_ordre = forms.CharField()
    annees_experience = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_medecin = True
        if commit:
            user.save()
            ProfilMedecin.objects.create(
                user=user,
                specialite=self.cleaned_data['specialite'],
                numero_ordre=self.cleaned_data['numero_ordre'],
                annees_experience=self.cleaned_data['annees_experience']
            )
        return user
