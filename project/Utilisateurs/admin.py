from django.contrib import admin
from .models import *
from .models import Utilisateur,Etudiant, projet, Cv,Enseignant,Entp as Entreprise,Connexion
from django.contrib import admin


   

admin.site.register(Utilisateur)
admin.site.register(Connexion)


admin.site.register(Etudiant)
admin.site.register(projet)
admin.site.register(Enseignant)
admin.site.register(Entreprise)


admin.site.register(Cv)
admin.site.register(Skill)
admin.site.register(Reference)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Experience)
admin.site.register(Award)
admin.site.register(Interest)
admin.site.register(Contact)
admin.site.register(Social)


# Register your models here.
