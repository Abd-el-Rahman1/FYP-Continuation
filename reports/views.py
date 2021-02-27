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
from .models import Report
from acc.forms import ReportCForm, CreateUserForm


# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def auditboard(request):
   reports = Report.objects.all()
   return render(request, 'auditboard.html', {'reports': reports})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def reportCreate(request):
   reports = Report.objects.all()
   #creation
   form = ReportCForm(initial={'creator':request.user})

   if request.method == 'POST':
      form = ReportCForm(request.POST)
      if form.is_valid():
         reports = form.save(commit=False)
         reports.creator = request.user
         Point.objects.create(pointOwner=request.user, dateCreated=datetime.datetime.now())
         form.save()
         return redirect('auditboard')

   return render(request, 'report_create.html',{'form': form, 'reports': reports,})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def reportView(request, pk):
   reports = Report.objects.get(id=pk)
   form = ReportCForm(instance=reports)
   return render(request, 'report_view.html',{'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def reportUpdate(request, pk):
    reports = Report.objects.get(id=pk)
    form = ReportCForm(instance=reports)
    if request.method == 'POST':
        form = ReportCForm(request.POST, instance=reports)
        if form.is_valid():
            reports.dateUpdated = datetime.datetime.now()
            if reports.closed == True:
                reports.dateFinished = datetime.datetime.now()
            Point.objects.create(pointOwner=request.user, dateCreated=datetime.datetime.now())                
            form.save()
            return redirect('auditboard')

    form = {'form':form}
    return render(request, 'report_update.html', form)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def reportDelete(request, pk):
    reports = Report.objects.get(id=pk)

    if request.method == 'POST':
        reports.delete()
        return redirect('auditboard')

    reports = {'reports':reports}
    return render(request, 'report_delete.html', reports)
