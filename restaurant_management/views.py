from django.stortcuts import render 
from django.config import settings

def home(request):
    return render (request , 'home.html',{
        'restaurent_name':settings.RESTAURANT_NAME
    })

def menu_list(request):
    menu_items = [
    {"name": "margherita jambo pizza", "price":500},
    {"name": "penne pasta", "price:400"},
    {"name": "veg burger", "price:200"},
    {"name": "chocolate brownie" ,"price:340"}
    ]
    return render(request,"menu.html",{"menu_items":menu_items})
    

def home(request):
    phone_number = settings.RESTAURANT_PHONE
    return render(request, 'home.html' , {'phone_number':phone_number})

def home(request):
    return render(request, 'home.html',
    {
        'restaurant_name':'KIKIS KITCHEN'
    })