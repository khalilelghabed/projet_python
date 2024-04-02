from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Cv
from .forms import CvForm  # Assuming you have a form for creating CVs



def creerUtilisateur(request):
    return HttpResponse('page de utilisateur')


# Create your views here.
@login_required
def view_cv(request):
    cv = Cv.objects.filter(utilisateur=request.user.utilisateur).first()

    if cv:
        context = {'cv': cv}
        return render(request, 'view_cv.html', context)
    else:
        return redirect('create_cv')  # Assuming the URL pattern name for creating CV is 'create_cv'
    

@login_required
def create_cv(request):
    if request.method == 'POST':
        form = CvForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.utilisateur = request.user.utilisateur
            cv.save()
            return redirect('view_cv')
    else:
        form = CvForm()
    
    context = {'form': form}
    return render(request, 'home/create_cv.html', context)