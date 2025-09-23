from rest_framework import generics , permissions
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer

class UserProfileSerializer(generics.UpdateAPIView)
    serializer_class = UserProfileSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user