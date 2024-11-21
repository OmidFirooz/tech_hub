from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('topic/<int:id>', views.topic_detail, name='topic_detail'),
    path('project/', views.project_detail, name='project_detail')
]
