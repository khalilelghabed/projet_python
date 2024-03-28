from django.urls import path
from . import views

urlpatterns = [
    path('creerPublication/',views.createPublication,name='creatPublication'),
    path('creer_commentaire/', views.creer_commentaire, name='creer_commentaire')
]
