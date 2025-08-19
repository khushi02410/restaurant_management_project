from django.db import models
from django.contrib.auth.models import User
from .models import MenuItem 
# Create your models here.

class Order(models.Model)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing' , 'Processing'),
        ('completed' , 'Completed'),
        ('cancelled' , 'Cancelled'),
    ]

    customer = models.ForeginKey(User , on_delete = models.CASADE)
    customer = models.ManyToManyFeild(MenuItem)
    total_amount = models.DecimalFeild(max_digit = 10 , decimal_places = 2)
    status = models.CharField(max_length = 20 , choices = STATUS_CHOICES , default = 'pending')
    created_at = models.DateTimeFeild(auto_now_add = True)

    def __str__ (self):
        reutrn f"Order {self.id} by {self.customer.username}"
