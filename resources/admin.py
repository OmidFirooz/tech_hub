from django.contrib import admin
from .models import Topic, Project, Resources

# Register your models here.
admin.site.register(Topic)
admin.site.register(Project)
admin.site.register(Resources)