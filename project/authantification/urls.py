from django.urls import path
from . import views

urlpatterns = [
    path('creerCompte/',views.creer_compte,name='creerCompte'),
    path('creercompteEntreprise/',views.creer_compteEntreprise,name='creercompteEntreprise'),
    path('login/',views.authentifier,name='authentificate'),
    path('logout/',views.logOut,name='logOut')
]
