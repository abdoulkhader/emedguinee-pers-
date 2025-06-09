from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    choix_inscription,
    register_patient,
    register_medecin,
    redirect_after_login,
    CustomLoginView
)

urlpatterns = [
    path('inscription/', choix_inscription, name='choix_inscription'),
    path('inscription/patient/', register_patient, name='register_patient'),
    path('inscription/medecin/', register_medecin, name='register_medecin'),
    path('login/', CustomLoginView.as_view(), name='login'),  # on garde seulement celui-ci
    path('redirect/', redirect_after_login, name='redirect_after_login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
