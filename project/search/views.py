from django.shortcuts import render
from Utilisateurs.models import Utilisateur, Etudiant, Enseignant

def search(request):
    if request.method == 'POST':
        
        search = request.POST.get('search')
         
        
        allUtilisatuer = Utilisateur.objects.filter(prenom=search)
        if allUtilisatuer.count() > 0:
                return render(request, 'search/search.html', {'utilisateurs': allUtilisatuer})
        else:
                 message = 'Il n y a aucun Etudiant correspondant avec ce nom.'
                 return render(request, 'search/search.html', {'message': message})
        
        
