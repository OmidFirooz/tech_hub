from django import forms
from .models import Topic, Resource, Project

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']
        
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'link', 'description']
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'github_link']