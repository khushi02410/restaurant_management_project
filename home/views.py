from django.shortcuts import render
from datetime import datetime
from .models import MenuItem
from products.models import MenuItem
from .models import Contact
from django.contrib import messages
from .models import MenuCategory 
from .serializers import MenuCategorySerializer
from rest_framework.views import APIView
form rest_framework.response import Response
from .serializers import MenuItemSerializer
from django.http import JsonResponse
from utils.validation_utils import is_valid_email
from rest_framework import status
# Create your views here.


def home_view(request):
    return render(request, 'home/home.html')
    return render(request, 'about.html')
    return render(request, 'contact.html')
    address = restaurantAddress.objects.first()
    return render(request, 'home.html' , {'address': address})

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            subject = f"New Contact Form Submission from {contact.name}"
            message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}"
            recipient_list = ["kikieskitchen@gmail.com"]

            send_mail(subject , message , setting.DEFAULT_FROM_EMAIL , recipient_list)
            
            return redirect('contact_success')
        else:
            form = ContactForm()
        return render(request, 'home/contact.html', {'form': form})

def home(request):
    menu_itemss = Menu.objects.all()
    return render(request, 'home/index.html', {'menu_items' : menu_items})

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        Contact.objects.create(name=name , email=email)
        return redirect("homepage")

    return render(request , "home.html")        


class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializers_class = MenuCategorySerializer

class MenuItemsByCategoryView(APIView):
    def get(self,request,*args,**kwargs)
    category_name = request.query_params.get('category',None)

    if not category_name:
        return Response(
            {"error":"category query parameter is required"},status=status.HTTP_400_BAD_REQUEST
        )

    items = MenuItem.objects.filter(category__name__iexact=category_name)
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)    


def subscribe_view(request):
    if request.mwthod = "POST"
        email = request.POST.get("email")
        if not is_valid_email:
            return JsonResponse({"error": "Invalid email address"}, status = 400)
        return JsonResponse({"message":"subscription successful!"})


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes= [permission.ISAdminUser]

    def update(self,request,*args,**kwargs):
        try:
            return super().update(request,*args, **kwargs)
        except Exception as e:
            return Response(
                {"error":str(e)},
                status=status.HTTPs_404_BAD_REQUEST
            )    