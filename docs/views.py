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
from .models import Doc
import documents
from acc.forms import DocCForm, CreateUserForm
from django.core.files.storage import FileSystemStorage
from pathlib import Path
import os
from django.utils import timezone


# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def docboard(request):
   docs = Doc.objects.all()
   return render(request, 'docboard.html', {'docs': docs})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Employee'])
def edocboard(request):
   docs = Doc.objects.filter(classified=False)
   return render(request, 'edocboard.html', {'docs': docs})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def docAdminCreate(request):
    docs = Doc.objects.all()
    #creation
    form = DocCForm(initial={'creator':request.user})
    if request.method == 'POST':
        form = DocCForm(request.POST, request.FILES)
        if form.is_valid():
            docs = form.save(commit=False)
            docs.creator = request.user                      
            a = ('{document}'.format(**form.cleaned_data))
            
            if Doc.objects.filter(name=a).exists():
                c = Doc.objects.filter(name=a, dateDeleted__isnull=True)               
                c.update(name = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+ '_' + a, dateDeleted = datetime.datetime.now()+ datetime.timedelta(days=100))

                docs.dateUpdated = datetime.datetime.now()
            Point.objects.create(pointOwner=request.user, dateCreated=datetime.datetime.now())
            docs.name = a
            form.save()
            return redirect('docboard')
        else:
            print (form.errors)

    return render(request, 'doc_create.html',{'form': form, 'docs': docs,})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Employee'])
def docEmployeeCreate(request):
    docs = Doc.objects.all()
    #creation
    form = DocCForm(initial={'creator':request.user})
    if request.method == 'POST':
        form = DocCForm(request.POST, request.FILES)
        if form.is_valid():
            docs = form.save(commit=False)
            docs.creator = request.user                      
            a = ('{document}'.format(**form.cleaned_data))
            
            if Doc.objects.filter(name=a).exists():
                c = Doc.objects.filter(name=a, dateDeleted__isnull=True)               
                c.update(name = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+ '_' + a, dateDeleted = datetime.datetime.now()+ datetime.timedelta(days=100))

                docs.dateUpdated = datetime.datetime.now()
            Point.objects.create(pointOwner=request.user, dateCreated=datetime.datetime.now())
            docs.name = a
            form.save()
            return redirect('edocboard')
        else:
            print (form.errors)

    return render(request, 'doc_e_create.html',{'form': form, 'docs': docs,})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def completeDelete(request):
    docs = Doc.objects.all()
    try:
        dDocs = Doc.objects.get(dateDeleted__lt = datetime.datetime.now(), document__isnull=False)
        for d in os.scandir(settings.MEDIA_ROOT):
            if dDocs.document == d:
                dDocs.delete()
                os.remove(d)
    except Doc.DoesNotExist:
        dDocs = None

    docs = {'docs':docs}
    return render(request, 'doc_view.html', docs)



@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def docDelete(request, pk):
    docs = Doc.objects.get(id=pk)   
    if request.method == 'POST':
        docs.dateDeleted = datetime.datetime.now() + datetime.timedelta(days=100)
        docs.save()
        return redirect('docboard')

    docs = {'docs':docs}
    return render(request, 'doc_delete.html', docs)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Employee'])
def edocDelete(request, pk):
    docs = Doc.objects.get(id=pk)   
    if request.method == 'POST':
        docs.dateDeleted = datetime.datetime.now() + datetime.timedelta(days=100)
        docs.save()
        return redirect('edocboard')

    docs = {'docs':docs}
    return render(request, 'doc_e_delete.html', docs)

