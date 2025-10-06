from django.urls import path
from .views import RequestRideAPIView, AvailableRidesAPIView, AcceptRideAPIView

urlpatterns = [
    path('api/ride/request/', RequestRideAPIView.as_view(), name='request_ride'),
    path('api/ride/available/', AvailableRidesAPIView.as_view(), name='available_rides'),
    path('api/ride/accept/<int:ride_id>/', AcceptRideAPIView.as_view(), name='accept_ride'),
]