from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all().order_by('-created')
    form = TaskForm()
    
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks:home')
    
    context = {'task': task, 'form': form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == "POST":
        task.delete()
        return redirect('tasks:home')
    
    
    context = {'task': task}
    return render(request, 'tasks/delete.html', context)