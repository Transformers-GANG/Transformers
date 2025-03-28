from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Link to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Fields for the user profile
    name = models.CharField(max_length=255)
    address = models.TextField()
    blood_group = models.CharField(max_length=3, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')])
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
