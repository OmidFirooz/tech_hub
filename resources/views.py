from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

from .models import Topic, Resource, Project  # Profile, Assuming you have models for these
from .forms import TopicForm, ResourceForm, ProjectForm


# Dashboard
@login_required
def dashboard(request):
    resources = Resource.objects.all().order_by('-created_at')
    projects = Project.objects.all().order_by('-created_at')
    topics = Topic.objects.all().order_by('-created_at')
    context = {
        'resources': resources,
        'projects': projects,
        'topics': topics,
    }
    
    print("Resources: ", resources)
    print("projects: ", projects)
    print("topics: ", topics)
    return render(request, 'resources/dashboard.html', context)



# Homepage
# @login_required
# def homepage(request):
#     resources = Resource.objects.all().order_by('-created_at')
#     projects = Project.objects.all().order_by('-created_at')
#     topics = Topic.objects.all().order_by('-created_at')
#     context = {
#         'resources': resources,
#         'projects': projects,
#         'topics': topics,
#     }
    
#     print("resources: ", resources)
#     print("projects: ", projects)
#     print("topics: ", topics)
#     return render(request, 'resources/test.html', context)
    

# Add Topic
@login_required
def add_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('resources:topics')
    else:
        form = TopicForm()
    return render(request, 'resources/add_topic.html', {'form': form})


# Add Resources
@login_required
def add_resources(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resources = form.save(commit=False)
            resources.user = request.user
            resources.save()
            return redirect('resources:resources')
    else:
        form = ResourceForm
    return render(request, 'resources/add_resources.html', {'form': form})


# Add Project
@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('resources:projects')
    else:
        form = ProjectForm()
    return render(request, 'resources/add_project.html', {'form': form})

# Homepage view (could be a simple landing page)
@login_required
def homepage(request):
    return render(request, 'resources/homepage.html')

# Topics Page
@login_required
def topics_view(request):
    # topics = Topic.objects.all()  # Fetch all topics from the database
    topics = Topic.objects.filter(user=request.user)
    return render(request, 'resources/topics.html', {'topics': topics})

# Topic detail
@login_required
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'resources/topic_detail.html', {'topic':topic})

# Resource detail
@login_required
def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'resources/resource_detail.html', {'resource':resource})

# Resources Page
@login_required
def resources_view(request):
    resources = Resource.objects.filter(user=request.user)  # Fetch all resources from the database
    return render(request, 'resources/resources.html', {'resources': resources})

# Projects Page
@login_required
def projects_view(request):
    projects = Project.objects.filter(user=request.user)  # Fetch all projects from the database
    return render(request, 'resources/projects.html', {'projects': projects})

# Project Detail Page
@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})