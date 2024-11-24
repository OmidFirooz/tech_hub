from django.db import models
from django.contrib.auth.models import User

# Topic Model
class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.name

# Resource Model
class Resource(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.TextField()
    file = models.FileField(upload_to='resources/files/', blank=True, null=True)
    image = models.ImageField(upload_to='resources/images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return self.title

# Project Model
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField()
    file = models.FileField(upload_to='projects/files/',blank=True, null=True)
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name
