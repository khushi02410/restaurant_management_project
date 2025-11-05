from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuCategory
from .models import MenuItem,Ingredient
from .models import Table
from .models import ContactFormSubmission


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id','name']

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedFeild()

    class Meta:
        model=MenuItem
        feilds = ['id' , 'name' , 'description','price','category','available', 'is_featured']

    def validation_price(self,value):
        if value <= 0:
            raise serializers.validationError("price must be a +tive number") 
        return value       

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['table_number', 'capacity', 'is_available']

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ['id', 'name', 'email', 'message', 'submitted_at']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_message(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Message must be at least 5 characters long.")
        return value        
    
class IngredienSerializer(serializers.ModelSerializer):    
    class meta:
        model = Ingredient
        fields = ['id','name']