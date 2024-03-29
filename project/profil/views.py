# from django.shortcuts import render
# from Utilisateurs.models import Utilisateur

# def profil_page(request):
#     utilisateurs = Utilisateur.objects.all()  # Query the utilisateur models
#     return render(request, 'profil/profileEtudiant.html', {'utilisateurs': utilisateurs})

# profil/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Utilisateurs.models import Utilisateur

def profil_page(request, user_id):
    utilisateur = Utilisateur.objects.get(id=user_id)
    is_own_profile = request.user == utilisateur.user  # Assuming you have a 'user' field in your Utilisateur model
    return render(request, 'profil/profileEtudiant.html', {'utilisateur': utilisateur, 'is_own_profile': is_own_profile})
