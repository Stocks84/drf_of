from django.contrib.auth.models import User
from rest_framework import serializers, permissions, viewsets

from users.serializers import UserProfileSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
