from django.contrib import admin
from .models import Utilisateur,Etudiant, projet, Cv,Enseignant
from django.contrib import admin


   

admin.site.register(Utilisateur)


admin.site.register(Etudiant)
admin.site.register(projet)
admin.site.register(Cv)
admin.site.register(Enseignant)



# Register your models here.
