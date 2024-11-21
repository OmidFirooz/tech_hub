from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Resources(models.Model):
    RESOURCES_TYPES = [
        ('Article', 'Article'),
        ('Video', 'Video'),
        ('Tutorial', 'Tutorial')
    ]
    title = models.CharField(max_length=100)
    descritption = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=50, choices=RESOURCES_TYPES)
    
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=50)
    github_link = models.URLField(blank=True)
    
    def __str__(self):
        return self.title