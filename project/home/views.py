from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Utilisateurs.models import Utilisateur
from django.db.models import Q  
from notification.models import Notification
from publications.models import Publication
def home(request):
   
    return render(request, 'home/home.html')

@login_required
def home_authentifie(request):
    utilisateur = request.user.utilisateur
    utilisateurs = Utilisateur.objects.all()
    all_notifications = utilisateur.notifier.all()
    count = 0
    for notification in all_notifications:
        if not notification.is_read:
            count += 1

    if utilisateur is not None:
        # Retrieve users that are following the current user and are being followed by the current user
        mutual_users = utilisateur.followers.filter(pk__in=utilisateur.following.values_list('pk', flat=True))
        
        # Retrieve publications of mutual_users
        publication_suivies = Publication.objects.filter(Q(auteur__in=mutual_users) | Q(auteur=utilisateur)).order_by('-date_publication')
        
        return render(request, "home/home_authentifie.html", {'publications': publication_suivies, 'utilisateurs': mutual_users, 'nombre_notifications_non_lues': count})
              
    else:
        # L'utilisateur n'a pas d'objet Utilisateur associé
        print("L'utilisateur n'a pas d'objet Utilisateur associé.")

    return render(request, "home/home_authentifie.html", {'utilisateurs': utilisateurs})


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
            message = f"{request.user.utilisateur.nom} {request.user.utilisateur.prenom} a réagi à votre publication."
            new_notification=Notification(utilisateur=publication.auteur,message=message)
            new_notification.save()

            
        publication.save()
        
        # Sérialiser les données de la publication mises à jour
        publication_data = {
            'id': publication.id,
            'nombre_react': publication.nombre_react,
            # Autres champs de publication que vous voulez renvoyer
        }

        # Retourner les données de la publication mises à jour en tant que réponse JSON
        return JsonResponse({'status': 'success', 'publication': publication_data})

# Dans views.py

from django.http import JsonResponse
from publications.models import Publication

def load_more_publications(request):
    page_number = int(request.GET.get('page', 1))
    publications_per_page = 10
    offset = (page_number - 1) * publications_per_page
    
    if offset < 0:
        offset = 0

    # Filtrer les publications suivies par l'utilisateur
    user_following = request.user.utilisateur.following.all()
    publications = Publication.objects.filter(auteur__in=user_following).order_by('-date_publication')[offset:offset + publications_per_page]

    serialized_publications = []
    for publication in publications:
        serialized_publication = {
            'id': publication.id,
            'content': publication.contenu,
            'auteur': {
                'id': publication.auteur.id,
                'nom': publication.auteur.nom,
                'prenom': publication.auteur.prenom,
                'photo_profil': publication.auteur.photo_profil.url if publication.auteur.photo_profil else None
            },
            'date': publication.date_publication.strftime('%B %d, %Y, %I:%M %p'),  # Format date as desired
            'likes': publication.nombre_react,
            'comments': publication.nombre_commentaires
        }
        serialized_publications.append(serialized_publication)

    return JsonResponse(serialized_publications, safe=False)