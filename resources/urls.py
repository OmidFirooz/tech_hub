from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    # homepage
    path('', views.dashboard, name='dashboard'),
    
    # article
    path('articles/', views.articles_view, name='articles'),
    path('article/<int:pk>/', views.article_detail, name="article_detail"),
    path('add-article/', views.add_article, name='add_article'),
    
    # Monograph
    path('monographs/', views.monographs_view, name='monographs'),
    path('monographs/<int:pk>', views.monograph_detail, name='monograph_detail'),
    path('add-monographs/', views.add_monograph, name="add_monograph"),

    # Project
    path('projects/', views.projects_view, name='projects'),
    path('add-project/', views.add_project, name='add_project'),
    path('projects/<int:pk>', views.project_detail, name='projects_detail'),
]