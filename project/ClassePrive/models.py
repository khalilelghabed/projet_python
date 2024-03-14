from django.db import models

class classePrive(models.Model):
    titre=models.CharField(max_length=256)
    nombre_max=models.IntegerField()
    nombre_etudiants=models.IntegerField()
    date_debut=models.DateTimeField( auto_now_add=True)
    date_fin=models.DateTimeField(auto_now_add=False)
    enseignant=models.ForeignKey('auth.user',on_delete=models.CASCADE,related_name='creation_classePrive')







# Create your models here.
