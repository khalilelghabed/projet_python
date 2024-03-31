from django.shortcuts import render, redirect
from django.http import  HttpResponse
from Utilisateurs.models import Utilisateur, Enseignant,Etudiant
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate, logout 

def creer_compte(request):
    if request.method == 'POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        confirmer = request.POST.get("password2")
        date_naissence = request.POST.get("date_naissenc")
        region = request.POST.get("region")
        type = request.POST.get("type")
        
        if password == confirmer:
            # Vérifier si un utilisateur avec le même email existe déjà
            if User.objects.filter(username=email).exists():
                # Générer un nom d'utilisateur unique en ajoutant un suffixe numérique
                username = email
                count = 1
                while User.objects.filter(username=username).exists():
                    username = f"{email}{count}"
                    count += 1
            else:
                username = email
                user = User.objects.create_user(
                    username=username,  # Utilisation de l'email comme nom d'utilisateur
                    email=email,
                    password=password
                )
                if type == 'etu':
                    etudiant = Etudiant.objects.create(
                        user=user,
                        nom=lastname,
                        prenom=firstname,
                        date_naissenc=date_naissence,
                        type_profil=type,
                        region=region
                    )
                    etudiant.save()
                if type == 'ens':
                    enseignant = Enseignant.objects.create(
                        user=user,
                        nom=lastname,
                        prenom=firstname,
                        type_profil=type,
                        date_naissenc=date_naissence,
                        region=region
                    )
                    enseignant.save()
                messages.success(request, "compte a été crée avec succes")
                return redirect('authentificate')
                
        else:
            messages.error(request, 'les deux mots de passe sont différents')
            return redirect('creerCompte')
    return render(request, 'login/creerCompte.html')


def authentifier(request):
  if request.method=='POST':
    email=request.POST.get('email')
    password=request.POST.get('password')
    utilisateur=authenticate(request,username=email,password=password)
    print (utilisateur)
    if utilisateur is not None:
       print("vous avez authentifie")
       login(request,utilisateur)
       return redirect('homeAuthentifie')
    else:
       return render(request, 'login/authentification.html', {'error_message': 'email ou mot pass incorrect'})
  return render(request,'login/authentification.html')


def logOut(request):
   logout(request)
   return redirect('home')
# Create your views here.
