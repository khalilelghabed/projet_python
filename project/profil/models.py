from django.db import models
from Utilisateurs.models import Enseignant, Etudiant

class Profil(models.Model):
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE, blank=True, null=True)
    enseignant = models.OneToOneField(Enseignant, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=500)
    
   
    def __str__(self):
        if self.etudiant:
            return f"{self.etudiant.nom} {self.etudiant.prenom}"
        elif self.enseignant:
            return f"{self.enseignant.nom} {self.enseignant.prenom}"
        else:
            return "Profil sans utilisateur associé"
    
    def save(self, *args, **kwargs):
        if self.etudiant is None and self.enseignant is None:
            raise ValueError("Un profil doit être lié à un étudiant ou à un enseignant.")
        if self.etudiant is not None and self.enseignant is not None:
            raise ValueError("Un profil ne peut être lié à la fois à un étudiant et à un enseignant.")
        super(Profil, self).save(*args, **kwargs)



# Create your models here.
