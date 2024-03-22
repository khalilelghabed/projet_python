from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/home.html')

@login_required
def home_authentifie(request):
    return render(request, "home/home_authentifie.html")
