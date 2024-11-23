from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('topics/', views.topics_view, name='topics'),
    path('topic/<int:pk>/', views.topic_detail, name="topic_detail"),
    path('resources/', views.resources_view, name='resources'),
    path('projects/', views.projects_view, name='projects'),
    # path('profile/', views.profile_view, name='profile'),
]