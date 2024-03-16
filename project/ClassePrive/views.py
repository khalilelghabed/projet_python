from django.shortcuts import render
from django.http import HttpResponse

def afficherClasseprive(request):
    return HttpResponse("le page de classe privé ")

# Create your views here.
