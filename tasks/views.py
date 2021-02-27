from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from acc.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
import datetime
from points.models import Point
from .models import Task
from acc.forms import TaskCForm


# Create your views here.


@login_required(login_url='login')
def taskCreate(request):
   tasks = Task.objects.all()
   #creation
   form = TaskCForm(initial={'creator':request.user})

   if request.method == 'POST':
      form = TaskCForm(request.POST)
      if form.is_valid():
         tasks = form.save(commit=False)
         tasks.creator = request.user
         Point.objects.create(pointOwner=request.user, dateCreated=datetime.datetime.now())
         form.save()
         return redirect('taskCreate')

   return render(request, 'task_create.html',{'form': form, 'tasks': tasks,})

@login_required(login_url='login')
def taskView(request, pk):
   tasks = Task.objects.get(id=pk)
   form = TaskCForm(instance=tasks)
   return render(request, 'task_view.html',{'form': form})

@login_required(login_url='login')
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskCForm(instance=tasks)
    if request.method == 'POST':
        form = TaskCForm(request.POST, instance=tasks)
        if form.is_valid():
            tasks.dateUpdated = datetime.datetime.now()
            if tasks.finished == True:
                tasks.dateFinished = datetime.datetime.now()
            Point.objects.create(pointOwner=request.user, dateCreated=datetime.datetime.now())                
            form.save()
            return redirect('taskCreate')

    form = {'form':form}
    return render(request, 'task_update.html', form)

@login_required(login_url='login')
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)

    if request.method == 'POST':
        tasks.delete()
        return redirect('taskCreate')

    tasks = {'task':tasks}
    return render(request, 'task_delete.html', tasks)
