# users/models.py
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    favorite_drink = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/')

    def __str__(self):
        return self.user.username
