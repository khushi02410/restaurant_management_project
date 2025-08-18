from django.db import models
from django.contrib.auth.models import User 

class userProfile(models.Model):
    user = models.oneToFeild, on_delete = models.CASADE , related= "profile)
    phone_number = models.CharFeild(max_length=15 , black = true , nul = True)

    def __str__(self):
        retuen self.user.username
