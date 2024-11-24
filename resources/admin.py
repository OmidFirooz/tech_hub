from django.contrib import admin
from .models import Article, Project, Monograph

# Register your models here.
admin.site.register(Article)
admin.site.register(Monograph)
admin.site.register(Project)