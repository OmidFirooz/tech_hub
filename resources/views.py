from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'resources/homepage.html')

def topic_detail(request, id):
    id = id
    return render(request, 'resources/topic_detail.html', {'id':id})

def project_detail(request, id):
    id = id
    return render(request, 'resources/project_detail.html', {'id':id})