from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'priority', 'completed')
    list_filter = ('completed', 'priority', 'due_date', 'user')
    search_fields = ('title', 'description', 'category')
    ordering = ('-due_date', '-priority', '-created_date')
