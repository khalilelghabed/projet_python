from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from Utilisateurs.models import Etudiant, Enseignant, Entreprise

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    description = models.TextField(max_length=500)
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE, blank=True, null=True)
    enseignant = models.OneToOneField(Enseignant, on_delete=models.CASCADE, blank=True, null=True)
    entreprise = models.OneToOneField(Entreprise, on_delete=models.CASCADE, blank=True, null=True)

    def clean(self):
        if not self.etudiant and not self.enseignant and not self.entreprise:
            raise ValidationError("Un profil doit être lié à un étudiant, un enseignant ou une entreprise.")
        if sum(bool(x) for x in [self.etudiant, self.enseignant, self.entreprise]) > 1:
            raise ValidationError("Un profil ne peut être lié qu'à un seul type d'utilisateur.")

    def __str__(self):
        if self.etudiant:
            return f"Profil de l'étudiant {self.etudiant}"
        elif self.enseignant:
            return f"Profil de l'enseignant {self.enseignant}"
        elif self.entreprise:
            return f"Profil de l'entreprise {self.entreprise}"


# Create your models here.
