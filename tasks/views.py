from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TaskForm
from .models import Task

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Create Task',
        'submit_text': 'Create'
    })

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
