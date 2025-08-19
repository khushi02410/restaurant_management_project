from django.db import models
from django.contrib.auth.models import User
from restaurant.models import MenuItem 
# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('processing','Processing'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    ]

        customer = models.ForeignKey(User , on_delete=models.CASCADE)
        order_items = models.ManyToManyField(MenuItem)
        total_amount = models.DecimalField(max_digits = 10 , decimal_places = 2)
        status = models.CharField(max_length = 20 , choices = STATUS_CHOICES , default = 'pending')
        created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"
