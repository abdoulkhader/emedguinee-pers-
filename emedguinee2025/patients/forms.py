from django import forms
from .models import RendezVous

class PriseRendezVousForm(forms.ModelForm):
    MOTIF_CHOICES = [
        ('consultation', 'Consultation générale'),
        ('suivi', 'Suivi'),
        ('examen', 'Résultats d’examen'),
        ('urgence', 'Urgence'),
        ('autre', 'Autre'),
    ]

    motif = forms.ChoiceField(
        choices=MOTIF_CHOICES,
        label='Motif du rendez-vous'
    )
    # Champ affiché uniquement si "Autre" est sélectionné
    motif_autre = forms.CharField(
        required=False,
        label='Précisez le motif',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex : Consultation post-opératoire'
        })
    )
    

    class Meta:
        model = RendezVous
        fields = ['medecin', 'date', 'motif']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'medecin': 'Choisir un médecin',
            'date': 'Date et heure',
        }


from django import forms
from .models import Patient

class ModifierProfilPatientForm(forms.ModelForm):
    email = forms.EmailField(label='Adresse email', required=True)

    class Meta:
        model = Patient
        fields = ['telephone']
        labels = {
            'telephone': 'Téléphone',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # on récupère l'utilisateur connecté
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['email'].initial = user.email  # pré-remplir le champ email

    def save(self, commit=True):
        patient = super().save(commit=False)
        self.user.email = self.cleaned_data['email']  # mettre à jour l'email User
        if commit:
            self.user.save()
            patient.save()
        return patient


from django import forms
from .models import MessagePatient

class ContactMedecinForm(forms.ModelForm):
    class Meta:
        model = MessagePatient
        fields = ['medecin', 'sujet', 'message']
        widgets = {
            'medecin': forms.Select(attrs={'class': 'form-control'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Objet du message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Votre message ici...'}),
        }