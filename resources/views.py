from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Resource, Project, Profile  # Assuming you have models for these

# Homepage view (could be a simple landing page)
def homepage(request):
    return render(request, 'resources/homepage.html')

# Topics Page
def topics_view(request):
    topics = Topic.objects.all()  # Fetch all topics from the database
    return render(request, 'resources/topics.html', {'topics': topics})

# Topic detail
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'resources/topic_detail.html', {'topic':topic})

# Resources Page
def resources_view(request):
    resources = Resource.objects.all()  # Fetch all resources from the database
    return render(request, 'resources/resources.html', {'resources': resources})

# Projects Page
def projects_view(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    return render(request, 'resources/projects.html', {'projects': projects})

# Profile Page (User Profile)
@login_required  # Ensure the user is logged in before accessing the profile page
def profile_view(request):
    user_profile = Profile.objects.get(user=request.user)  # Fetch the logged-in user's profile
    return render(request, 'resources/profile.html', {'profile': user_profile})
