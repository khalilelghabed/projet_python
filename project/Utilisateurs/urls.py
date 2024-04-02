from django.urls import path
from .views import *
# , view_cv, create_cv

urlpatterns = [
    path('',creerUtilisateur,name='creerUtilisateur'),
    path('view-cv/',view_cv, name='view_cv'),
    path('create-cv/', create_cv, name='create_cv'),
    path('edit_page/', edit_page, name='edit_page'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    
    path('edit_skill/', edit_skill, name='edit_skill'),
    path('edit_reference/', edit_reference, name='edit_reference'),
    path('edit_education/', edit_education, name='edit_education'),
    path('edit_certification/', edit_certification, name='edit_certification'),
    path('edit_social/', edit_social, name='edit_social'),

]