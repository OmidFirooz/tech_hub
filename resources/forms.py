from django import forms
from .models import Article, Monograph, Project

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'user', 'abstract', 'file']
        
class MonographForm(forms.ModelForm):
    class Meta:
        model = Monograph
        fields = ['title', 'user', 'abstract', 'file']
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'user', 'github_link', 'abstract', 'file']