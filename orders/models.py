from django.db import models
from django.contrib.auth.models import User
from restaurant.models import MenuItem 
from restaurant_management import RestauranntLocation
# Create your models here.

class Menu(models.model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    name = models.CharField(max_length = 40 , unique = True)

    def __str__(self):
        return self.name


class Order(models.Model):
 
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    order_items = models.ManyToManyField(Menu)
    order_date = models.DateTimeField(auto_now_add = True)
    total_amount = models.DecimalField(max_digits = 10 , decimal_places = 2)
    status = models.CharField(max_length = 20 , choices = [("pending","Pending"),("completed","Completed"),("cancelled","Cancelled")],default="pending"
    )
    # created_at = models.DateTimeField(auto_now_add = True)

    restaurant = models.ForeignKey(
        RestauranntLocation,
        on_delete=models.CASCADE,
        related_name = "orders"
    )

    status = models.ForeignKey(
        OrderStatus,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"
        return f"Order by {self.customer_name} at {self.restaurant.city} on {self.order_date}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True , null = True)
    price = models.DecimalField(max_digits = 6 , decimal_places = 2) 
    image = models.ImageField(upload_to ='menu_images/', blank = True , null=True )

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=30,unique=True)
    discount = 
