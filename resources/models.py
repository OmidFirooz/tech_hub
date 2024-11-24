from django.db import models
from django.contrib.auth.models import User

# Topic Model
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    file = models.FileField(upload_to='articles/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Resource Model
class Monograph(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='monographs')
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    file = models.FileField(upload_to='articles/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Project Model
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=200)
    abstract = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='projects/files/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name