from django.contrib import admin
from .models import Utilisateur,Etudiant, projet, Cv,Enseignant,Entreprise
from django.contrib import admin


   

admin.site.register(Utilisateur)


admin.site.register(Etudiant)
admin.site.register(projet)
admin.site.register(Cv)
admin.site.register(Enseignant)
admin.site.register(Entreprise)


# Register your models here.
