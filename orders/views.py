from django.shortcuts import render
from .models import MenuItem
from .models import Order
from .serializers import OrderSerializer
from .utils  import send_order_confirmation_email
from rest_framework.generics import RetriveAPIView
from rest_framework].permissions import IsAuthenticated

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

class OrderHistoryView(generics.ListAPIView)
    serializer_class = OrderSerializer
    permission_classes = [permissions_IsAuthentication]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-date')
        
class OrderDetailView(RetriveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"        