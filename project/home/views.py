from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    
    return render(request, 'home/home.html')
@login_required
def home_authentifie(request):
    publication_suivies=[]
    utilisateur = request.user.utilisateur
    if utilisateur is not None:
        # L'utilisateur a un objet Utilisateur associé
        following = utilisateur.following.all()
        if following.count() > 0 :
            for utilisateur in following:
                publication_suivies.extend(utilisateur.user.publier.all())
                print(publication_suivies)
                for publication in publication_suivies:

                    print(publication)
            
            
           
        
    else:
        # L'utilisateur n'a pas d'objet Utilisateur associé
        following = None
        print("L'utilisateur n'a pas d'objet Utilisateur associé.")

    return render(request, "home/home_authentifie.html")

