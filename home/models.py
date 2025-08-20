from django.db import models
from django.contrib.auth.models import User 

class userProfile(models.Model):
    user = models.oneToFeild, on_delete = models.CASADE , related_name= "profile)
    phone_number = models.CharFeild(max_length=15 , black = true , nul = True)

    def __str__(self):
        retuen self.user.username

class OpeningHours(models.Model):
    days = model.CharFeild(max_length=100)
    hours = models.CharFeild(max_length=100)

    def __str__(self):
        return f"{self.days}: {self.hours}"