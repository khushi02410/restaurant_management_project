from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    STATUS_CHOICES = [
        ('REQUESTED', 'Requested'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    rider = models.ForeignKey(User, related_name='rides_requested', on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name='rides_accepted', on_delete=models.SET_NULL, null=True, blank=True)
    
    pickup_address = models.CharField(max_length=255)
    dropoff_address = models.CharField(max_length=255)
    
    pickup_lat = models.DecimalField(max_digits=9, decimal_places=6)
    pickup_lng = models.DecimalField(max_digits=9, decimal_places=6)
    drop_lat = models.DecimalField(max_digits=9, decimal_places=6)
    drop_lng = models.DecimalField(max_digits=9, decimal_places=6)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')
    
    requested_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status} ({self.pickup_address} → {self.dropoff_address})"