from django.db import models
from Utilisateurs.models import Utilisateur

class Publication(models.Model):
  
    contenu=models.TextField()
    date_publication=models.DateTimeField(auto_now_add=True , null=False, blank=False   )
    nombre_react=models.IntegerField(default=0, null=False , blank=False)
    nombre_commentaires=models.IntegerField(default=0 , null=False , blank=False )
    auteur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE,related_name='publier')
    media=models.FileField(upload_to='publications/publications_medias',null=True,blank=True)
    fichier=models.FileField(upload_to='publications/publications_fichiers',null=True,blank=True)
    interacteurs = models.ManyToManyField(Utilisateur, related_name='publications_aimées', blank=True)
    


class Commentaire(models.Model):
    contenu=models.TextField(max_length=500)
    date=models.DateField( auto_now_add=True)
    auteur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    nombre_react=models.IntegerField(default=0)
    publication=models.ForeignKey(Publication,on_delete=models.CASCADE,related_name='commentaires')
    

class Repense(models.Model):
    contenu=models.TextField(max_length=500)
    date=models.DateField( auto_now_add=True)
    auteur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    nombre_react=models.IntegerField(default=0)
    commentaire=models.ForeignKey(Commentaire,on_delete=models.CASCADE,related_name='repenses')
    

class Like(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'publication')  # Assure que chaque utilisateur ne peut liker une publication qu'une seule fois


