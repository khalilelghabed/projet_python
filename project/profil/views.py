from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Utilisateurs.models import Utilisateur,Etudiant,User,Enseignant,Entreprise
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
def update_information_etu(request, user_id):
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
        portfolio = request.POST.get('portfolio')
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
        if major:
            etudiant.major = major
        if gender:
            etudiant.GENDER_CHOICES = gender
        if institution:
            etudiant.institution = institution
        if portfolio:
            etudiant.portfolio = portfolio
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

@login_required
def update_information_ens(request, user_id):
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
        institution2 = request.POST.get('institution2')
        specialty = request.POST.get('specialty')
        portfolio2 = request.POST.get('portfolio2')
        experiences2 = request.POST.get('experiences2')
        
        # Récupérer l'enseignant associé à l'utilisateur actuel
        enseignant = Enseignant.objects.get(user=request.user)
        
        # Vérifier chaque champ avant de l'affecter à l'objet Enseignant
        if photo_profil:
            folder = 'photos/photos_Profil/'
            img = request.FILES["photo_profil"]
            fs = FileSystemStorage(location=folder)
            fs.save(img.name, img)
            enseignant.photo_profil = photo_profil

        if name:
            enseignant.nom = name
        if prenom:
            enseignant.prenom = prenom 
        if bio:
            enseignant.bio = bio 
        if email:
            enseignant.email = email
        if tel:
            enseignant.tele = tel
        if date_birthay:
            enseignant.date_naissenc = date_birthay
        if gender:
            enseignant.GENDER_CHOICES = gender
        if institution2:
            enseignant.institution2 = institution2
        if specialty:
            enseignant.specialty = specialty
        if portfolio2:
            enseignant.portfolio2 = portfolio2
        if experiences2:
            enseignant.experiences2 = experiences2
       
        
        
        enseignant.save()  # Sauvegarder les modifications
        
          # Vous pouvez imprimer ou effectuer d'autres actions avec major si nécessaire
        
        # Rediriger vers la page de profil avec l'ID de l'utilisateur
        return redirect('profil_page', user_id=user_id)
    else:
        # Rediriger vers la page de profil si la méthode de la requête n'est pas POST
        return redirect('profil_page', user_id=user_id)


    
    
    
    
    

@login_required
def update_information_ent(request, user_id):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        photo_profil = request.FILES.get('photo_profil')
        company_name = request.POST.get('company_name')
        owner_name = request.POST.get('owner_name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        tel = request.POST.get('tel')
        website3 = request.POST.get('website3')
        size = request.POST.get('size')
        specialties = request.POST.get('specialties')
        certifications = request.POST.get('bio')
        location = request.POST.get('location')
        working_days = request.POST.get('working_days')
       
        
        # Récupérer l'enseignant associé à l'utilisateur actuel
        entreprise = Entreprise.objects.get(user=request.user)
        
        # Vérifier chaque champ avant de l'affecter à l'objet entreprise
        if photo_profil:
            folder = 'photos/photos_Profil/'
            img = request.FILES["photo_profil"]
            fs = FileSystemStorage(location=folder)
            fs.save(img.name, img)
            entreprise.photo_profil = photo_profil

        if company_name:
            entreprise.company_name = company_name
        if owner_name:
            entreprise.owner_name = owner_name 
        if bio:
            entreprise.bio = bio 
        if email:
            entreprise.email = email
        if tel:
            entreprise.tele = tel
        if website3:
            entreprise.website3 = website3
        if size:
            entreprise.size = size
        if specialties:
            entreprise.specialties = specialties
        if certifications:
            entreprise.certifications = certifications
        if location:
            entreprise.location = location
        if working_days:
            entreprise.working_days = working_days
      
       
        
        
        entreprise.save()  # Sauvegarder les modifications
        
          # Vous pouvez imprimer ou effectuer d'autres actions avec major si nécessaire
        
        # Rediriger vers la page de profil avec l'ID de l'utilisateur
        return redirect('profil_page', user_id=user_id)
    else:
        # Rediriger vers la page de profil si la méthode de la requête n'est pas POST
        return redirect('profil_page', user_id=user_id)

# def profil_search(request):
    
#     email = request.POST.get('search')
#     print(request.user)
#     utilisateur = User.objects.get(username=email)
#     utilisateur = Utilisateur.objects.get(user=utilisateur)
#     print(utilisateur)
#     is_own_profile = request.user == utilisateur.user  
#     print(is_own_profile)# Assuming you have a 'user' field in your Utilisateur model
#     return render(request, 'profil/profileEtudiant.html', {'utilisateur': utilisateur, 'is_own_profile': is_own_profile})
    