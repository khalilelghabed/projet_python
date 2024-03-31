from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Utilisateurs.models import Utilisateur


from publications.models import Publication
def home(request):
    
    return render(request, 'home/home.html')
@login_required
def home_authentifie(request):
    publication_suivies = []
    utilisateurs = Utilisateur.objects.all()

    # Check if there's a search query
    search_query = request.GET.get('q')
    if search_query:
        utilisateurs = utilisateurs.filter(nom__icontains=search_query) | utilisateurs.filter(prenom__icontains=search_query)

    if request.user.utilisateur:
        following = request.user.utilisateur.following.all()
        if following.count() > 0:
            for utilisateur in following:
                publication_suivies.extend(utilisateur.publier.all())

    return render(request, "home/home_authentifie.html", {'publications': publication_suivies, 'utilisateurs': utilisateurs, 'search_query': search_query})


from django.http import JsonResponse

def ajouter_like(request, publication_id):
    if request.method == 'POST':
        # Logique pour ajouter le like à la publication
        publication = Publication.objects.get(pk=publication_id)
        if request.user.utilisateur in publication.interacteurs.all():
            publication.nombre_react-=1
            publication.interacteurs.remove(request.user.utilisateur)
        else: 
            publication.nombre_react += 1
            publication.interacteurs.add(request.user.utilisateur)

        
        publication.save()

        # Sérialiser les données de la publication mises à jour
        publication_data = {
            'id': publication.id,
            'nombre_react': publication.nombre_react,
            # Autres champs de publication que vous voulez renvoyer
        }

        # Retourner les données de la publication mises à jour en tant que réponse JSON
        return JsonResponse({'status': 'success', 'publication': publication_data})
