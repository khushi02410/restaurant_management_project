from django.shortcuts import render
from .models import MenuItem
from .models import Order
from .serializers import OrderSerializer
from .utils  import send_order_confirmation_email
from rest_framework.generics import RetriveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import coupon
from .serializers import CouponSerializer
from django.shortcuts import get_object_or_404

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

class CouponValidationView(APIView):
    def post(self , request , *args , **kwargs):
        code = request.data.get("code" , "").strip()

        if node code:
            return Response(
                {"error":"Coupon code is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            coupon = Coupon.objects.get(code__iexact=code)
        except Coupon.DoesNotExist:
            return Response(
                {"error":"Invalid coupon code"},
                status=status.HTTP_400_BAD_REQUEST
            )

        today = timezone.now().date()
        if not coupon.is_active:
            return Response(
                {"error": "This coupon is not ative"},
                status = status.HTTP_400_BAD_REQUEST
            )
        if today < coupon.valid_from or today > coupon.valid_until:
            return Response(
                {"error":"This coupon is not valid at this point "},
                status = status.HTTP_400_BAD_REQUEST
            )

        serializer = CouponSerializer(coupon )
        return Response(
            {"success": True , "coupon":serializer.data},
            staus =status.HTTP_200_OK
        )

class CancelOrderAPIView(views.APIView):
    Permission_class = [IsAuthenticated]

    def delete(self, request, order_id):
        order = get_object_or_404(Order , id=order_id)

        if order.user != request.user:
            return Response(
                {"error":"you are not authorized to cancel this order."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        if order.status == 'CANCELLED':
            return Response(
                {"error":"This order is already cancelled."}
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if order.status == 'COMPLETED':
            return Response(
                {"error":"Completed order cannot be cancelled."},status=status.HTTP_400_BAD_REQUEST
            )
        
        order.status = 'CANCELLED'
        order.save()

        return Response(
            {"message":f"Order {order.order_id} has been cancelled successfully."},status=status.HTTP_200_OK
        )