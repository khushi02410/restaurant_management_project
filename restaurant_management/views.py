from django.stortcuts import render 
from django.config import settings
from rest_framework.views import APIView
from rest_framework.response import Response

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
    address = RestaurantAddress.objects.first()

    return render(request, 'home.html',
    {
        'restaurant_name': settings.'KIKIS KITCHEN'
        "restaurant_address": settings.RESTAURANT_ADDRESS
        "address": address
    })
    return render(request,"home.html" , context)

class MenuAPIView(APIView):
    def get(self,request):
        menu=[
            {"name":"margherita pizza" , "description":"Classic cheese and tomato pizza","price ": 250},
            {"name": "panner tikka" , "description ": "grilled cottage cheeze with spices", "price":300},
            {"name": "pasta alfredo" , "description": "creamy white sause pasta", "price": 450},
            {"nmae": "veg burger" , "description": "burger with fresh fries and veggies" , "price" : 500},
        ]
        return Response(menu)