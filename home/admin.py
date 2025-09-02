from django.contrib import admin
from .models import UserProfile
from .models import RestaurantAddress

admin.site.register(UserProfile)

class RestaurantAddressAdmin(admin.ModelAdmin):
    list_display = ("address" , "city" , "state" , "zipcode")


