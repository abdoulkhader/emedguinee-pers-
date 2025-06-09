from django.urls import path
from .views import dashboard_patient
from .views import dashboard_patient, prendre_rdv_patient  # ✅ ici
from .views import profil_patient
from .views import mes_rendez_vous
from .views import dashboard_patient, dossier_medical
from django.contrib.auth.views import LogoutView
from .views import modifier_profil_patient  # à importer si pas déjà fait




urlpatterns = [
    
    path('dashboard/', dashboard_patient, name='patient_dashboard'),
    path('prendre-rdv/', prendre_rdv_patient, name='prise_rdv_patient'),
    path('profil/', profil_patient, name='profil_patient'),
    path('mes-rendez-vous/', mes_rendez_vous, name='mes_rendez_vous'),
    path('profil/', profil_patient, name='profil_patient'),
    path('dossier-medical/', dossier_medical, name='dossier_medical'),  # 🔵 ajout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('modifier-profil/', modifier_profil_patient, name='modifier_profil_patient'),
]
