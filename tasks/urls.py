from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('create/', views.task_create, name='task_create'),
    path('', views.task_list, name='task_list'),
] 