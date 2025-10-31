from django.db import models
from django.contrib.auth.models import User

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

class MenuItem(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digit=5, decimal_places=2)
    category = models.ForeignKey(MenuCategory,on_delete=models.CASCADE, related_name = "items")
    available = models.BooleanFeild(default=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

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
    
