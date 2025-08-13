from django.shortcuts import render
from datetime import datetime
# Create your views here.


def home_view(request):
    return render(request, 'home/home.html')
    return render(request, 'about.html')
    return render(request, 'contact.html')

def home(request):
    return render(request 'home.html',
    {
        'restaurant_name':'KIKIS KITECHEN'
    })  

def home(request):
    return render(request, 'home/home.html',{'current_year': datetime.now().year})

def about(request):
    return render(request, 'home/about.html',{'current_year': datetime.now().year})

def contact(request):
    return render(request,'home/contact.html':{'current_year': datetime.now().year})

def menu(request):
    return render(request,'home/menu.hmtl':{'current_year': datetime.now().year})

def reservations(request):
    return render(request,'home/reservations.html':{'current_year': datetime.now().year})

