from django.urls import path
from .views import *
from .views import menu_view
from .views import OrderHistoryView
from .views import OrderDetailView

urlpatterns = [
    path('menu/' , menu_view , name='menu'),
    path('order-history/', OrderHistoryView.as_view(), name='order-history'),
    path("order/<int:id>/" , OrderDetailView.as_view() , name="order-detail"),
    path("coupon/validate/" , CouponValidationView.as_view(), name='coupon-validate'),
    path('api/orders/<int:order_id>/cancel/', CancelOrderAPIView.as_view(), name='cancel_order'),
]