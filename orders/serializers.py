from rest_framework import serializers 
from .models import Order, OrderItem 

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id' , 'menu_item' , 'quantity', 'price']
        