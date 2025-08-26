from django.contrib import admin
from .models import Menu , Order 
from .models import MenuItem

# Register your models here.
admin.site.register(MenuItem)

class MenuAdmin(admin.ModelAdmin):
    list_display = ("name","price","description")
    search_fields = ("name",)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id" , "customer" , "total_amount" , "status")
    list_filter = ("status",)
    search_fields = ("customer__username",)
        
