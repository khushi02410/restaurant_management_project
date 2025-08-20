from django.contrib import admin
from .models import Menu , Order 
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ("name","price","description")
    search_fields = ("name",)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id" , "customer" , "total_amount" , "status")
    list_filter = ("status",)
    search_fields = ("customer__username",)
        
