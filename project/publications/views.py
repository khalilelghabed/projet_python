from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Publication
from django.contrib import messages
def createPublication(request):
    if request.method == 'POST':
        print("La méthode s'applique")
        user = request.user
        contenu = request.POST.get('contenu')
        publication = Publication(auteur=user, contenu=contenu)
        publication.save()
        messages.success(request, "Publication a été créée avec succès.")
        return redirect('homeAuthentifie')        
    else:
        print("Erreur: méthode non autorisée")
        return HttpResponse(status=405)  
   
   

# Create your views here.
        


