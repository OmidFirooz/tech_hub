from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Topic, Resources, Project
# Create your views here.

def homepage(request):
    topics = Topic.objects.all()
    return render(request, 'resources/homepage.html', {'topics':topics})

def topic_detail(request, id):
    topic = get_object_or_404(Topic, id=id)
    resources = Resources.objects.filter(topic=topic)
    return render(request, 'resources/topic_detail.html', {'topic':topic, 'resources': resources})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'resources/project_detail.html', {'project':project})