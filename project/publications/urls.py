from django.urls import path
from . import views

urlpatterns = [
    path('creerPublication/',views.createPublication,name='creatPublication')
]
