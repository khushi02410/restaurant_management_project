from django.shortcuts import render

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