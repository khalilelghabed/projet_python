from django.db import models


class Publication(models.Model):
    titre=models.CharField(max_length=255)
    contenu=models.TextField()
    date_publication=models.DateTimeField(auto_now_add=True)
    nombre_react=models.IntegerField(default=0)
    nombre_commentaires=models.IntegerField(default=0)
    auteur=models.ForeignKey('auth.user',on_delete=models.CASCADE)


class Commentaire(models.Model):
    contenu=models.TextField(max_length=500)
    date=models.DateField( auto_now_add=True)
    auteur=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    nombre_react=models.IntegerField(default=0)
    publication=models.ForeignKey(Publication,on_delete=models.CASCADE,related_name='commentaires')
    

class Repense(models.Model):
    contenu=models.TextField(max_length=500)
    date=models.DateField( auto_now_add=True)
    auteur=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    nombre_react=models.IntegerField(default=0)
    commentaire=models.ForeignKey(Commentaire,on_delete=models.CASCADE,related_name='repenses')
    


# Create your models here.
