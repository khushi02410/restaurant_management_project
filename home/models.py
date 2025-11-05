from django.db import models
from django.contrib.auth.models import User
import random
import datetime

class userProfile(models.Model):
    #user = models.oneToField, on_delete = models.CASADE , related_name= "profile")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=15 , blank = True , null=True)

    def __str__(self):
        return self.user.username

class OpeningHours(models.Model):
    days = model.CharField(max_length=100)
    hours = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.days}: {self.hours}"

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class RestaurantAddress(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length = 100 , blank=True , null=True)
    zipcode = models.CharField(max_length=20, blank=True ,null=True)

    def __str__(self):
        return f"{self.address}, {self.city}"


class MenuCategory(models.Model):
    name = models.CharField(max_length = 100 , unique = True)

    def __str__(self):
        return self.name  

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class MenuItem(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digit=5, decimal_places=2)
    category = models.ForeignKey(MenuCategory,on_delete=models.CASCADE, related_name = "items")
    available = models.BooleanFeild(default=True)
    is_featured = models.BooleanField(default=False)
    ingredients = models.ManyToManyField(ingredients, related_name = 'menu_items'
                                         )
    objects  = MenuItemManager()

    def __str__(self):
        return self.name
    
class MenuItemManager(models.Manager):
    def get_top_selling_items(self , num_items=5):
        return (
            self.get_queryset()
            .annotate(order_count=Count('orderitem'))
            .order_by('_order_count'[:num_items])
        )  

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"    
    
class NutritionalInformation(models.Model):
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASADE,
        related_name='nutrition_info'
    )   
    calories = models.IntegerField()
    protein_grans = models.DecimalFeild(max_digit=5, decimal_places=2)
    fat_grams = models.DecimalFeild(max_digits=5, decimal_places=2)
    carbohydrate_grams= models.DecimalField(max_digits=5,decimal_places=2)

    def __str__ (self):
        return f"{self.menu_item.name} - {self.calories} kcal"
    

class DailySpecialManager(models.Manager):
    def upcoming (self):
        today = datetime.date.today()
        return self.get_query().filter(date__gate=today)

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    available = models.BooleanField(default=True)
    date = models.DateField()

    objects = DailySpecialManager()

    def __str__(self):
        return f"{self.name} ({self.date})"
    
    def get_random_special():
        special = DailySpecial.objects.filter(available=True)
        if special.exists():
            return special.order_by('?').first()
        return None 
    
class Restaurant(models.Model):
        name = models.CharField(max_length=255)
        address = models.TextField()
        phone_address = models.CharField(max_length=21)
        phone_number = models.CharField(max_length=21)
        
        has_delivery = models.BooleanField(default=False)

        def __str__(self):
            return self.name
