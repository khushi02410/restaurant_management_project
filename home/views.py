from django.shortcuts import render
from datetime import datetime
from .models import MenuItem
# Create your views here.


def home_view(request):
    return render(request, 'home/home.html')
    return render(request, 'about.html')
    return render(request, 'contact.html')

def home(request):
    return render(request 'home.html',
    {
        'restaurant_name':'KIKIS KITECHEN'
    }

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

def menu_view(request):
    try:
        items = MenuItem.objects.all()
        return render(request, 'menu.html',{'items':items})
    except Exception as e:
        #log the error for debugging
        print(f"Error fetching menu items: {e}")

        return HttpResponse("Sorry, we could't load the menu right now.")

def contact_view(request):
    return render(request, 'home/contact.html')
