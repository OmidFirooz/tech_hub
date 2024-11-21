from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse('<h1>Homepage is Working</h1>')

def topic_detail(request):
    return HttpResponse('<h1>Topic detail is Working</h1>')

def project_detail(request):
    return HttpResponse('<h1>project detail is Working</h1>')