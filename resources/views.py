from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

from .models import Article, Monograph, Project  # Profile, Assuming you have models for these
from .forms import ArticleForm, MonographForm, ProjectForm


# Dashboard
@login_required
def dashboard(request):
    monographs = Monograph.objects.all().order_by('-created_at')
    projects = Project.objects.all().order_by('-created_at')
    articles = Article.objects.all().order_by('-created_at')
    context = {
        'monographs': monographs,
        'projects': projects,
        'articles': articles,
    }
    return render(request, 'resources/dashboard.html', context)



# Add article
@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('resources:articles')
    else:
        form = ArticleForm()
    return render(request, 'resources/add_article.html', {'form': form})


# Article Page
@login_required
def articles_view(request):
    articles = Article.objects.filter(user=request.user)
    return render(request, 'resources/articles.html', {'articles': articles})

# Article detail
@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'resources/article_detail.html', {'article':article})


# Add Monographs
@login_required
def add_monograph(request):
    if request.method == 'POST':
        form = MonographForm(request.POST, request.FILES)
        if form.is_valid():
            resources = form.save(commit=False)
            resources.user = request.user
            resources.save()
            return redirect('resources:monographs')
    else:
        form = MonographForm
    return render(request, 'resources/add_monograph.html', {'form': form})



# Monograph Page
@login_required
def monographs_view(request):
    monographs = Monograph.objects.filter(user=request.user)  # Fetch all resources from the database
    return render(request, 'resources/monographs.html', {'monographs': monographs})

# Monograph detail
@login_required
def monograph_detail(request, pk):
    monograph = get_object_or_404(Monograph, pk=pk)
    return render(request, 'resources/monograph_detail.html', {'monograph':monograph})

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


# Projects Page
@login_required
def projects_view(request):
    projects = Project.objects.filter(user=request.user)  # Fetch all projects from the database
    return render(request, 'resources/projects.html', {'projects': projects})

# Project Detail Page
@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'resources/project_detail.html', {'project': project})