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
from .models import Project
from acc.forms import ProjectCForm


# Create your views here.


@login_required(login_url='login')
def projectCreate(request):
   projects = Project.objects.all()
   #creation
   form = ProjectCForm(initial={'creator':request.user})

   if request.method == 'POST':
      form = ProjectCForm(request.POST)
      if form.is_valid():
         projects = form.save(commit=False)
         projects.creator = request.user
         Point.objects.create(pointOwner=request.user, dateCreated=datetime.datetime.now())
         form.save()
         return redirect('projectCreate')

   return render(request, 'project_create.html',{'form': form, 'projects': projects,})

@login_required(login_url='login')
def projectView(request, pk):
   projects = Project.objects.get(id=pk)
   form = ProjectCForm(instance=projects)
   return render(request, 'project_view.html',{'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
def projectUpdate(request, pk):
    projects = Project.objects.get(id=pk)
    form = ProjectCForm(instance=projects)
    if request.method == 'POST':
        form = ProjectCForm(request.POST, instance=projects)
        if form.is_valid():
            projects.dateUpdated = datetime.datetime.now()
            if projects.finished == True:
                projects.dateFinished = datetime.datetime.now()
            form.save()
            return redirect('projectCreate')

    form = {'form':form}
    return render(request, 'project_update.html', form)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
def projectDelete(request, pk):
    projects = Project.objects.get(id=pk)

    if request.method == 'POST':
        projects.delete()
        return redirect('projectCreate')

    projects = {'project':projects}
    return render(request, 'project_delete.html', projects)
