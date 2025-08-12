from django.stortcuts import render 
from django.config import settings

def home(request):
    return render (request , 'home.html',{
        'restaurent_name':settings.RESTAURENT_NAME
    })
