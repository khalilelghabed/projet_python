from django import forms
from .models import Cv

class CvForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ['nom', 'prenom', 'date_naissance', 'email', 'telephone', 'comptences', 'experiences', 'formaion', 'langues', 'centre_interet']
