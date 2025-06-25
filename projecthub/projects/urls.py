from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='dashboard'),  # homepage
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('register/', views.register, name='register'),
    path('projects/<int:pk>/toggle-pin/', views.toggle_pin, name='toggle_pin'),
    path('projects/new/', views.create_project, name='create_project'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('delete/', views.delete_projects, name='delete_projects'),
]

path('project/<int:pk>/', views.project_detail, name='project_detail'),


# Register URL
path('register/', views.register, name='register'),


path('projects/create/', views.create_project, name='create_project'),
