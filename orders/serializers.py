from rest_framework import serializers 
from .models import Order, OrderItem 
from .models import Coupon

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source="menu_item.name", read_only = True)
    class Meta:
        model = OrderItem
        fields = ['id' , 'menu_item' , 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True , read_only = True , source = "orderitem_set")

    class Meta:
        model = Order
        fields = ['id','date','total_price','items']
        depth = 1      

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code' , 'discount_percentage','valid_form','valid_until','is_active']        