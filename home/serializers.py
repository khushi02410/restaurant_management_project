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
        feilds = ['id' , 'name' , 'description','price','category']