# from django.shortcuts import render
# from Utilisateurs.models import Utilisateur

# def profil_page(request):
#     utilisateurs = Utilisateur.objects.all()  # Query the utilisateur models
#     return render(request, 'profil/profileEtudiant.html', {'utilisateurs': utilisateurs})

# profil/views.py

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Utilisateurs.models import Utilisateur,Etudiant
from django.core.files.storage import FileSystemStorage

def profil_page(request, user_id):
    print(request.user)
    utilisateur = Utilisateur.objects.get(id=user_id)
    print(utilisateur)
    is_own_profile = request.user == utilisateur.user  
    print(is_own_profile)# Assuming you have a 'user' field in your Utilisateur model
    return render(request, 'profil/profileEtudiant.html', {'utilisateur': utilisateur, 'is_own_profile': is_own_profile})

from datetime import datetime
@login_required
def update_information(request, user_id):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        photo_profil = request.FILES.get('photo_profil')
        name = request.POST.get('name')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        tel = request.POST.get('tel')
        date_birthay = request.POST.get('date_birthay')
        gender = request.POST.get('gender')
        institution = request.POST.get('institution')
        major = request.POST.get('major')
        year_study = request.POST.get('year_study')
        degree = request.POST.get('degree')
        top_skills = request.POST.get('top_skills')
        experiences = request.POST.get('experiences')
        
        # Récupérer l'étudiant associé à l'utilisateur actuel
        etudiant = Etudiant.objects.get(user=request.user)
        
        # Vérifier chaque champ avant de l'affecter à l'objet Etudiant
        if photo_profil:
            folder = 'photos/photos_Profil/'
            img = request.FILES["photo_profil"]
            fs = FileSystemStorage(location=folder)
            fs.save(img.name, img)
            etudiant.photo_profil = photo_profil

        if name:
            etudiant.nom = name
        if prenom:
            etudiant.prenom = prenom 
        if bio:
            etudiant.bio = bio 
        if email:
            etudiant.email = email
        if tel:
            etudiant.tele = tel
        if date_birthay:
            etudiant.date_naissenc = date_birthay
        if gender:
            etudiant.GENDER_CHOICES = gender
        if institution:
            etudiant.institution = institution
        if year_study:
            etudiant.year_of_study = year_study
        if degree:
            etudiant.degree = degree
        if top_skills:
            etudiant.top_skills = top_skills
        if experiences:
            etudiant.experiences = experiences
        
        
        etudiant.save()  # Sauvegarder les modifications
        
        print(major)  # Vous pouvez imprimer ou effectuer d'autres actions avec major si nécessaire
        
        # Rediriger vers la page de profil avec l'ID de l'utilisateur
        return redirect('profil_page', user_id=user_id)
    else:
        # Rediriger vers la page de profil si la méthode de la requête n'est pas POST
        return redirect('profil_page', user_id=user_id)













