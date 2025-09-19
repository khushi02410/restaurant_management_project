from django.db import models
from django.contrib.auth.models import User 

class userProfile(models.Model):
    user = models.oneToField, on_delete = models.CASADE , related_name= "profile)
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
    
