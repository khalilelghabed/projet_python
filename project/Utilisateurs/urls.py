from django.urls import path
from . views import creerUtilisateur

urlpatterns = [
    path('',creerUtilisateur,name='creerUtilisateur')
]