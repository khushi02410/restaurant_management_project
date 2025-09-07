from django.shortcuts import render
from .models import MenuItem

# Create your views here.
path('/orders',OrdersListView.as_view(),name='orders'),

def menu_view(request):
    item = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})
    
def home_view(request):
    query = request.GET.get("q")
    if query:
        menu_items = MenuItem.objects.filter(name__icontaind=query)
    else:
        menu_items = MenuItem.objects.all()

    # featured_items = MenuItem.objects.all()[:3]
    return render(request, 'home.html' , {'menu_items': menu_items, "query": query})