from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import TaskForm, TaskFilterForm
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
    tasks = Task.objects.filter(user=request.user)
    filter_form = TaskFilterForm(request.GET)
    
    if filter_form.is_valid():
        status = filter_form.cleaned_data['status']
        priority = filter_form.cleaned_data['priority']
        category = filter_form.cleaned_data['category']
        
        if status:
            tasks = tasks.filter(completed=(status == 'completed'))
        if priority:
            tasks = tasks.filter(priority=priority)
        if category:
            tasks = tasks.filter(category__icontains=category)
    
    tasks = tasks.order_by('-created_date')
    
    context = {
        'tasks': tasks,
        'filter_form': filter_form
    }
    return render(request, 'tasks/task_list.html', context)
