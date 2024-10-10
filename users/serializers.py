from django.contrib.auth.models import User
from users.models import UserProfile
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'first_name', 'last_name', 'bio', 
            'favorite_drink', 'location', 'profile_image', 
            'date_of_birth', 'date_joined', 'is_active', 'is_staff'
        ]
        read_only_fields = ['date_joined', 'is_active', 'is_staff']
