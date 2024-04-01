from django.shortcuts import render
from Utilisateurs.models import Utilisateur, Etudiant, Enseignant

def search(request):
    if request.method == 'POST':
        type_search = request.POST.get('type_search')
        search = request.POST.get('search')
        
        if type_search == 'Etu':
            allUtilisatuer = Etudiant.objects.filter(nom=search)
            if allUtilisatuer.count() > 0:
                return render(request, 'search/search.html', {'utilisateurs': allUtilisatuer})
            else:
                message = 'Il n y a aucun Etudiant correspondant avec ce nom.'
                return render(request, 'search/search.html', {'message': message})
        
        elif type_search == 'ens':
            allUtilisatuer = Enseignant.objects.filter(nom=search)
            if allUtilisatuer.count() > 0:
                return render(request, 'search/search.html', {'utilisateurs': allUtilisatuer})
            else:
                message = 'Il n y a aucun Enseignant correspondant avec ce nom.'
                return render(request, 'search/search.html', {'message': message})
