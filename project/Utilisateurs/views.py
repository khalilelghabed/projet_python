from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Cv,Utilisateur

from .forms import CvForm,SkillForm, ReferenceForm,EducationForm, CertificationForm, ExperienceForm, AwardForm, InterestForm, ContactForm, SocialForm



def creerUtilisateur(request):
    return HttpResponse('page de utilisateur')




@login_required
def view_cv(request):
    cv = Cv.objects.filter(utilisateur=request.user.utilisateur).first()

    if cv:
        context = {
            'cv': cv,
            'skills': cv.skills.all(),
            'references': cv.references.all(),
            'educations': cv.educations.all(),
            'certifications': cv.certifications.all(),
            'experiences': cv.experiences.all(),
            'awards': cv.awards.all(),
            'interests': cv.interests.all(),
            'contact': cv.contact,
            'social': cv.social
        }
        return render(request, 'home/cv_view.html', context)
    else:
        # If the user does not have a CV, redirect them to create one
        return redirect('create_cv')

@login_required
def create_cv(request):
    if request.method == 'POST':
        cv_form = CvForm(request.POST)
        contact_form = ContactForm(request.POST)
        social_form = SocialForm(request.POST)
        # Include other forms as needed

        if cv_form.is_valid() and contact_form.is_valid() and social_form.is_valid():
            cv = cv_form.save(commit=False)
            cv.utilisateur = request.user.utilisateur
            cv.save()
            # Save contact and social info associated with the CV
            contact = contact_form.save()
            social = social_form.save()
            cv.contact = contact
            cv.social = social
            cv.save()
            # Redirect the user to view their newly created CV
            return redirect('view_cv')
    else:
        cv_form = CvForm()
        contact_form = ContactForm()
        social_form = SocialForm()
        # Instantiate other forms as needed

    context = {
        'cv_form': cv_form,
        'contact_form': contact_form,
        'social_form': social_form,
        # Pass other forms to the context as needed
    }
    return render(request, 'home/create_cv.html', context)


def edit_page(request):
    return render(request, 'home/edit_page.html')


@login_required
def edit_profile(request):
    # Retrieve the current user's Utilisateur instance
    utilisateur_instance = Utilisateur.objects.get(user=request.user)
    
    # Retrieve or create the Cv instance associated with the Utilisateur instance
    cv_instance, created = Cv.objects.get_or_create(utilisateur=utilisateur_instance)
    
    if request.method == 'POST':
        form = CvForm(request.POST, request.FILES, instance=cv_instance)
        if form.is_valid():
            form.save()
            return redirect('view_cv')  # Redirect to the profile page after editing
    else:
        form = CvForm(instance=cv_instance)
    
    return render(request, 'edit_cv/edit_profile.html', {'form': form})


@login_required
def edit_skill(request):
    utilisateur_instance = Utilisateur.objects.get(user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.utilisateur = utilisateur_instance
            skill.save()
            return redirect('view_cv')  # Redirect to the profile page after editing
    else:
        form = SkillForm()
    return render(request, 'edit_cv/edit_skill.html', {'form': form})

@login_required
def edit_reference(request):
    utilisateur_instance = Utilisateur.objects.get(user=request.user)
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            reference = form.save(commit=False)
            reference.utilisateur = utilisateur_instance
            reference.save()
            return redirect('view_cv')  # Redirect to the profile page after editing
    else:
        form = ReferenceForm()
    return render(request, 'edit_cv/edit_reference.html', {'form': form})

@login_required
def edit_education(request):
    utilisateur_instance = Utilisateur.objects.get(user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.utilisateur = utilisateur_instance
            education.save()
            return redirect('view_cv')  # Redirect to the profile page after editing
    else:
        form = EducationForm()
    return render(request, 'edit_cv/edit_education.html', {'form': form})

@login_required
def edit_certification(request):
    utilisateur_instance = Utilisateur.objects.get(user=request.user)
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.utilisateur = utilisateur_instance
            certification.save()
            return redirect('view_cv')  # Redirect to the profile page after editing
    else:
        form = CertificationForm()
    return render(request, 'edit_cv/edit_certification.html', {'form': form})

# Repeat the same pattern for other classes

@login_required
def edit_social(request):
    utilisateur_instance = Utilisateur.objects.get(user=request.user)
    if request.method == 'POST':
        form = SocialForm(request.POST)
        if form.is_valid():
            social = form.save(commit=False)
            social.utilisateur = utilisateur_instance
            social.save()
            return redirect('view_cv')  # Redirect to the profile page after editing
    else:
        form = SocialForm()
    return render(request, 'edit_cv/edit_social.html', {'form': form})