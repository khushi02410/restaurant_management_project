from rest_framework import serializers 
from .models import Order, OrderItem 

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id' , 'menu_item' , 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True , read_only = True , source = "orderitem_set")

    class Meta:
        model = Order
        fields = ['id','date','total_price','items']
                