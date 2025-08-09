
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
]
