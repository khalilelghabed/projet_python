from django.urls import path
from . import views

urlpatterns = [
    path('',views.creer_compte,name='creerCompte')
]
