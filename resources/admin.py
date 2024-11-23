from django.contrib import admin
from .models import Topic, Project, Resource

# Register your models here.
admin.site.register(Topic)
admin.site.register(Project)
admin.site.register(Resource)
# admin.site.register(Profile)