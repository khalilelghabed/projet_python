from django.db import models
from Utilisateurs.models import Enseignant,Etudiant

class ClassePrive(models.Model):
    titre=models.CharField(max_length=256)
    nombre_max=models.IntegerField()
    nombre_etudiants=models.IntegerField()
    date_creation=models.DateTimeField(auto_now_add=False)
    enseignant=models.ForeignKey(Enseignant,on_delete=models.CASCADE,related_name='creation_classePrive')
    etuidants=models.ManyToManyField(Etudiant)
    def __str__(self):
        return self.titre
    
class CourEnligne(models.Model):
    titre=models.CharField( max_length=100)
    date_debut=models.DateTimeField( auto_now=False, auto_now_add=False)
    date_fin=models.DateTimeField( auto_now=False, auto_now_add=False)
    nombre_participant=models.IntegerField()
    class_prive=models.ForeignKey(ClassePrive,  on_delete=models.CASCADE)
     
    def __str__(self) :
        return self.titre


class Annonce(models.Model):
    titre=models.CharField( max_length=100)
    contenu=models.TextField()
    fichier=models.FileField(upload_to='Annonces', max_length=100)
    date_ajoute=models.DateTimeField( auto_now=False, auto_now_add=True)
    classe_prive=models.ForeignKey(ClassePrive,  on_delete=models.CASCADE)
    def __str__(self) :
        return self.titre

# Create your models here.
