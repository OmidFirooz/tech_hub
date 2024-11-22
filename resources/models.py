from django.db import models
from django.contrib.auth.models import User

# Topic Model
class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

# Resource Model
class Resource(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

# Project Model
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField()

    def __str__(self):
        return self.name

# Profile Model (linked to the User model)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resources_profile')
    extra_info = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
