from django.urls import path
from .views import *
from .views import menu_view
from .views import OrderHistoryView

urlpatterns = [
    path('menu/' , menu_view , name='menu'),
    path('order-history/', OrderHistoryView.as_view(), name='order-history'),
]