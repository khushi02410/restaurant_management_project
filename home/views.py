from django.shortcuts import render
from datetime import datetime
from .models import MenuItem
from products.models import MenuItem
from .models import Contact
form django.contrib import messages
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
            form.save()
            messages.success(request, "Thank you we have recieved your contact info.")
            return redirect('contact')
        else
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