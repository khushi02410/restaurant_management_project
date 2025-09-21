from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id','name']

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedFeild()

    class Meta:
        model=MenuItem
        feilds = ['id' , 'name' , 'description','price','category','available']

    def validation_price(self,value):
        if value <= 0:
            raise serializers.validationError("price must be a +tive number") 
        return value       
