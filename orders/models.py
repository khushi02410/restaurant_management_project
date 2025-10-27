from django.db import models
from django.contrib.auth.models import User
from restaurant.models import MenuItem 
from restaurant_management import RestauranntLocation
from decimal import Decimal
from django.conf import settings
from home.models import MenuItem
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

    order_id = models.CharField(max_length=12, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    order_items = models.ManyToManyField(Menu)
    order_date = models.DateTimeField(auto_now_add = True)
    total_amount = models.DecimalField(max_digits = 10 , decimal_places = 2)
    #created_at = ActiveOrderManager()
    objects = models.Manager()

    status = models.CharField(max_length = 20 , choices = [("pending","Pending"),("completed","Completed"),("cancelled","Cancelled")],default="pending"
    )

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]
    # created_at = models.DateTimeField(auto_now_add = True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )

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
        return f"Order #{self.id} - {self.user.username}"
        return f"Order #{self.id} by {self.customer.name}"
        return f"Order by {self.customer_name} at {self.restaurant.city} on {self.order_date}"
        return f"Order {self.id} - {self.status}"
        return f"Order #{self.order_id} - {self.status}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True , null = True)
    price = models.DecimalField(max_digits = 6 , decimal_places = 2) 
    image = models.ImageField(upload_to ='menu_images/', blank = True , null=True )

    def __str__(self):
        return self.name

def calculate_total(self):
    total = Decimal('0.00')
    for item in self.items.all():
        total += item.price * item.quantity
    return total

class Coupon(models.Model):
    code = models.CharField(
        max_length=30,
        unique=True
    )

    discount = models.DecimalField(
        max_digits = 5,
        decimal_places = 2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()
     

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}%"

    def is_valid(self):
        today = timezone.now().date()
        return (
            self.is_active
            and self.valid_from <= today <= self.valid_until
        )   

class ActiveOrderManager(model.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending','processing'])

class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE ,related_name="items")
    menu_item = models.ForeignKey(MenuItem , on_delete = models.CASCADE)
    quantity = models.positiveIntegerFeild(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def  __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"