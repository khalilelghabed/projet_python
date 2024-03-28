from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),

    path('home',views.home_authentifie,name="homeAuthentifie"),
     path('ajouter-like/<int:publication_id>/', views.ajouter_like, name='ajouter_like'),

]
