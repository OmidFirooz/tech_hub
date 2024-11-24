from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    # path('', views.homepage, name='homepage'),
    path('', views.dashboard, name='dashboard'),
    path('topics/', views.topics_view, name='topics'),
    path('topic/<int:pk>/', views.topic_detail, name="topic_detail"),
    path('add-topic/', views.add_topic, name='add_topic'),
    path('resources/', views.resources_view, name='resources'),
    path('resources/<int:pk>', views.resource_detail, name='resource_detail'),
    path('add-resources/', views.add_resources, name="add_resources"),
    path('projects/', views.projects_view, name='projects'),
    path('add-project/<int:pk>', views.add_project, name='project_detail'),
    path('projects/', views.projects_view, name='projects'),
]