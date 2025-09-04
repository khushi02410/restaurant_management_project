from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length= 200)
    street = models.CharField(max_length=255)
    address = models.CharField(max_length = 252)
    city = models.CharField(max_length = 100)
    state  = models.CharField(max_length = 100)
    zip_code = models.CharField(max_length = 20)
    opening_hours = models.JSONField(default = dict)

    def __str__(self):
        return f"{self.address}, {self.name}, {self.city}, {self.state} - {self.zip_code}"
        
        
