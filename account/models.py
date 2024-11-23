from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account_profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    github_link = models.URLField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

