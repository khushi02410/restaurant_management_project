from django.contrib import admin
from .models import UserProfile
from .models import RestaurantAddress
from .models import Restaurant

admin.site.register(UserProfile)

class RestaurantAddressAdmin(admin.ModelAdmin):
    list_display = ("address" , "city" , "state" , "zipcode", "has_delivery")


