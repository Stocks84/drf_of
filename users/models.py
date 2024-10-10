from django.db import models

# Create your models here.

# This is the user profile where the username is the uique ID.
class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True, null=True)
    favorite_drink = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    date_of_birth = models.DateField()
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    def __str__(self):
        return self.username

    @property
    # To make sure the user is over the age of 18.
    def is_adult(self):
        import datetime
        today = datetime.date.today()
        return (today.year - self.date_of_birth.year) - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)) >= 18