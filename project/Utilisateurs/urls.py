from django.urls import path
from .views import creerUtilisateur, view_cv, create_cv

urlpatterns = [
    path('',creerUtilisateur,name='creerUtilisateur'),
    path('view-cv/',view_cv, name='view_cv'),
    path('create-cv/', create_cv, name='create_cv'),

]