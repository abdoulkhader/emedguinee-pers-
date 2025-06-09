from django.urls import path
from .views import dashboard_medecin
from .views import liste_medecins


urlpatterns = [
    path('dashboard/', dashboard_medecin, name='medecin_dashboard'),
    path('liste/', liste_medecins, name='liste_medecins'),
]
