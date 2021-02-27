from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from points.models import Point
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from django import template
from django.contrib.auth.models import Group 
from docs.models import Doc
from reports.models import Report
from risks.models import Risk
from projects.models import Project
from tasks.models import Task
from custs.models import Customer

# Create your views here.

def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.date_joined = datetime.datetime.now()
            form.save()
            messages.success(request,'Account created for: ' + {form.clean_data.get('username')})

            return redirect('login')
        
    context = {'form': form}
    return render (request, 'register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect! Please try again.')

    context = {}
    return render (request, 'login.html', context)

def logoutSite(request):
    logout(request)
    return redirect('login')


    ###

def userPage(request):
    risks = Risk.objects.all()
    docs = Doc.objects.all()
    reports = Report.objects.all()
    pobjs = Project.objects.all()
    tasks = Task.objects.all()
    custs = Customer.objects.all()
    points = Point.objects.all()

    risksT = risks.filter(status='Open').count() + risks.filter(status = 'Inprogress').count()
    docsT = docs.filter(dateDeleted__isnull=True).count()
    reportsT = reports.filter(closed=False).count()
    pobjsT = pobjs.filter(finished=False).count()
    tasksT = tasks.filter(finished=False).count()
    custsT = custs.filter(status='Inprogress').count()
    pointsT = points.filter(pointOwner=request.user.id).count()

    return render(request, 'user.html', {
        'risksT': risksT,
        'docsT': docsT,
        'reportsT': reportsT,
        'pobjsT': pobjsT,
        'tasksT': tasksT,
        'pobjs': pobjs,
        'tasks': tasks,
        'custsT': custsT,
        'pointsT': pointsT
        })

@login_required(login_url='login')
@admin_only
def home(request):
    risks = Risk.objects.all()
    docs = Doc.objects.all()
    reports = Report.objects.all()
    pobjs = Project.objects.all()
    tasks = Task.objects.all()
    custs = Customer.objects.all()
    points = Point.objects.all()

    risksT = risks.filter(status='Open').count() + risks.filter(status = 'Inprogress').count()
    docsT = docs.filter(dateDeleted__isnull=True).count()
    reportsT = reports.filter(closed=False).count()
    pobjsT = pobjs.filter(finished=False).count()
    tasksT = tasks.filter(finished=False).count()
    custsT = custs.filter(status='Inprogress').count()
    pointsT = points.filter(pointOwner=request.user.id).count()

    return render(request, 'dashboard.html', {
        'risksT': risksT,
        'docsT': docsT,
        'reportsT': reportsT,
        'pobjsT': pobjsT,
        'tasksT': tasksT,
        'pobjs': pobjs,
        'tasks': tasks,
        'custsT': custsT,
        'pointsT': pointsT
        
        
        })


@login_required(login_url='login')
def prefChart(request):
    pobj = Point.objects.annotate(month=ExtractMonth('dateCreated')).values('month').annotate(count=Count('dateCreated'))
    ps = []  
    for p in pobj:
        keys, values = zip(*p.items())
        ps.append(values)
    
    month, count = map(list, zip(*ps))
    data1={
        "months": month,
        "performance": count
    }
    
    return JsonResponse(data1)



@login_required(login_url='login')
def perPersonChart(request):
    #filtered_object = Point.objects.filter(pointOwner = request.user.id)
    pobj = Point.objects.filter(pointOwner = request.user.id).annotate(month=ExtractMonth('dateCreated')).values('month').annotate(count=Count('dateCreated'))
    ps = []  
    for p in pobj:
        keys, values = zip(*p.items())
        ps.append(values)
    
    month, count = map(list, zip(*ps))
    data2={
        "months": month,
        "performance": count
    }
    
    return JsonResponse(data2)


@login_required(login_url='login')
def totalP(request):
    #filtered_object = Point.objects.filter(pointOwner = request.user.id)
    pobj1 = Point.objects.annotate(month=ExtractMonth('dateCreated')).values('month').annotate(count=Count('dateCreated'))
    pobj2 = Point.objects.filter(pointOwner = request.user.id).annotate(month=ExtractMonth('dateCreated')).values('month').annotate(count=Count('dateCreated'))

    ps1 = []  
    for p in pobj1:
        keys, values = zip(*p.items())
        ps1.append(values)

    month, count = map(list, zip(*ps1))
    data1={
        "months": month,
        "performance": count
    }

    ps2 = [] 
    for p in pobj2:
        keys, values = zip(*p.items())
        ps2.append(values)

    month, count = map(list, zip(*ps2))
    data2={
        "months": month,
        "performance": count
    }

    total={
        "pref1": data1,
        "pref2": data2
    }
    
    return JsonResponse(total)