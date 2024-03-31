from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Publication,Commentaire
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Utilisateurs.models import Utilisateur
from notification.models import Notification

@login_required
def createPublication(request):
    if request.method == 'POST':
        print("La méthode s'applique")
        user = request.user.utilisateur
        contenu = request.POST.get('contenu')
        fichier=request.POST.get('fichier')
        media=request.POST.get('media')
        publication = Publication(auteur=user, contenu=contenu,fichier=fichier, media=media)
        publication.save()
        messages.success(request, "Publication a été créée avec succès.")
        return redirect('homeAuthentifie')        
    else:
        print("Erreur: méthode non autorisée")
        return HttpResponse(status=405)  

@login_required
@csrf_exempt
def creer_commentaire(request):
    if request.method == 'POST':
        contenu = request.POST.get('contenu')
        utilisateur_id = request.POST.get('utilisateur')
        publication_id = request.POST.get('publication_id')

        utilisateur = Utilisateur.objects.get(id=utilisateur_id)
        
        try:
            # Récupérer l'objet Publication
            publication = Publication.objects.get(id=publication_id)
            publication.nombre_commentaires += 1
            publication.save()
            
            # Créer un nouveau commentaire associé à la publication
            nouveau_commentaire = Commentaire.objects.create(
                contenu=contenu,
                auteur=utilisateur,
                publication=publication
            )
            message = f"{request.user.utilisateur.nom} {request.user.utilisateur.prenom} a commenté votre publication."

            new_notification=Notification(utilisateur=publication.auteur,message=message)
            new_notification.save()

            publication_data = {
                'id': publication.id,
                'nombre_commentaires': publication.nombre_commentaires
            }
            
            # Retourner une réponse JSON avec les données du commentaire nouvellement ajouté
            return JsonResponse({
                'message': 'Le commentaire a été créé avec succès.',
                'publication': publication_data,
                'commentaire': {
                    'photo_profil': utilisateur.photo_profil.url,
                    'auteur': utilisateur.nom + ' ' + utilisateur.prenom,
                    'date': nouveau_commentaire.date,  # Assurez-vous de récupérer la date correcte
                    'contenu': nouveau_commentaire.contenu
                }
            })
        
        except Publication.DoesNotExist:
            # Si la publication avec l'ID spécifié n'existe pas, renvoyer une erreur
            return JsonResponse({'error': 'La publication spécifiée n\'existe pas.'}, status=404)
    else:
        # Si la méthode n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
