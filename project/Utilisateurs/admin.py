from django.contrib import admin
<<<<<<< HEAD
from .models import *
=======
from .models import Utilisateur,Etudiant, projet, Cv,Enseignant,Entreprise
from django.contrib import admin
>>>>>>> f96709138bb8176d8029d3c16d41490796ec7735


   

admin.site.register(Utilisateur)


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
