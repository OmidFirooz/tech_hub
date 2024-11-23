from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('topics/', views.topics_view, name='topics'),
    path('topic/<int:pk>/', views.topic_detail, name="topic_detail"),
    path('resources/', views.resources_view, name='resources'),
    path('projects/', views.projects_view, name='projects'),
    path('add-topic/', views.add_topic, name='add_topic'),
    path('add-resources/', views.add_resources, name="add_resources"),
    path('add-project/', views.add_project, name='add_project')
]