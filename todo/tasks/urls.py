# Define URLS of 'tasks' app.

from django.urls import path
from . import views


app_name = "tasks"
urlpatterns = [
    # Home page.
    path('', views.index, name="home"),
    
    # Update task.
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    # Delete task.
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
]