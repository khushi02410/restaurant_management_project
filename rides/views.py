rom rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Ride
from .serializers import RideSerializer

# 1️⃣ Rider books a new ride
class RequestRideAPIView(generics.CreateAPIView):
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(rider=self.request.user, status='REQUESTED')


# 2️⃣ Drivers get all available (unassigned) rides
class AvailableRidesAPIView(generics.ListAPIView):
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ride.objects.filter(status='REQUESTED', driver__isnull=True)


# 3️⃣ Driver accepts a ride
from rest_framework.views import APIView

class AcceptRideAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ride_id):
        try:
            ride = Ride.objects.get(id=ride_id)
        except Ride.DoesNotExist:
            return Response({"error": "Ride not found."}, status=status.HTTP_404_NOT_FOUND)

        if ride.status != 'REQUESTED' or ride.driver is not None:
            return Response({"error": "Ride already accepted or unavailable."}, status=status.HTTP_400_BAD_REQUEST)

        ride.driver = request.user
        ride.status = 'ONGOING'
        ride.save()

        serializer = RideSerializer(ride)
        return Response(serializer.data, status=status.HTTP_200_OK)