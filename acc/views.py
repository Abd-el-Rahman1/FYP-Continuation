#This system is made by Abd-el-Rahman Mohammed Mohammed Abd-ell-Gabbar
#TP: TP049556

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
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


@unauthenticated_user
def loginPage(request):
#This code will validate the user input 
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

#this is the dashboard for the Employees
def userPage(request):
    #tables are called
    pobjs = Project.objects.all()
    tasks = Task.objects.all()
    custs = Customer.objects.all()
    points = Point.objects.all()

    #tables are filtered based on finished status
    pobjsF = pobjs.filter(finished=False).count()
    pobjsT = pobjs.filter(finished=True).count()
    tasksF = tasks.filter(finished=False).count()
    tasksT = tasks.filter(finished=True).count()
    custsT = custs.filter(status='In progress').count() + custs.filter(status='Open').count()
    pointsT = points.filter(pointOwner=request.user.id).count()

    return render(request, 'user.html', {
        'pobjsF': pobjsF,
        'pobjsT': pobjsT,
        'tasksF': tasksF,
        'tasksT': tasksT,
        'pobjs': pobjs,
        'tasks': tasks,
        'custsT': custsT,
        'pointsT': pointsT
        })


#This is the dashboard for Managers and Audits
@login_required(login_url='login')
@admin_only
def home(request):
    #tables are loaded
    risks = Risk.objects.all()
    reports = Report.objects.all()
    pobjs = Project.objects.all()
    tasks = Task.objects.all()
    custs = Customer.objects.all()
    points = Point.objects.all()

    #tables are filtered
    risksT = risks.filter(status='Open').count() + risks.filter(status='In progress').count()
    risksH = risks.filter(priority = 'High' ).count() + risks.filter(priority = 'Very High' ).count()
    risksL = risks.filter(priority = 'Low' ).count() + risks.filter(priority = 'Very Low' ).count()
    reportsNCR = reports.filter(closed=False).count() + reports.filter(NCR_or_OFI='NCR').count()
    reportsOFI = reports.filter(closed=False).count() + reports.filter(NCR_or_OFI='OFI').count()
    pobjsF = pobjs.filter(finished=False).count()
    pobjsT = pobjs.filter(finished=True).count()
    tasksF = tasks.filter(finished=False).count()
    tasksT = tasks.filter(finished=True).count()
    custsT = custs.filter(status='In progress').count() + custs.filter(status='Open').count()
    pointsT = points.filter(pointOwner=request.user.id).count()

    return render(request, 'dashboard.html', {
        'risksT': risksT,
        'risksH': risksH,
        'risksL': risksL,
        'reportsNCR': reportsNCR,
        'reportsOFI': reportsOFI,
        'pobjsF': pobjsF,
        'pobjsT': pobjsT,
        'tasksF': tasksF,
        'tasksT': tasksT,
        'pobjs': pobjs,
        'custsT': custsT,
        'pointsT': pointsT
        })

#This is responsible for sending the JSON response to the front-end
@login_required(login_url='login')
def prefChart(request):
    #table is filtered based on date
    pobj = Point.objects.annotate(month=ExtractMonth('dateCreated')).values('month').annotate(count=Count('dateCreated'))
    #This list is going to contain the data filtered after zipping
    ps = []  
    for p in pobj:
        keys, values = zip(*p.items())
        ps.append(values)
    
    month, count = map(list, zip(*ps))
    data1={
        "months": month,
        "performance": count
    }
    #data is sent as Json
    return JsonResponse(data1)



@login_required(login_url='login')
def perPersonChart(request):
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
def riskPer(request):
    risks = Risk.objects.all()

    risksO = risks.filter(status='Open').count() + risks.filter(status__isnull=True).count()
    risksI = risks.filter(status = 'In progress').count()
    risksC = risks.filter(status='Closed').count()

    riskslist={
        "open": risksO,
        "in_prog": risksI,
        "closed": risksC
    }
    
    return JsonResponse(riskslist)

@login_required(login_url='login')
def customerPer(request):
    custs = Customer.objects.all()

    custsO = custs.filter(status='Open').count() + custs.filter(status__isnull=True).count()
    custsI = custs.filter(status = 'In progress').count()
    custsC = custs.filter(status='Closed').count()

    custslist={
        "open": custsO,
        "in_prog": custsI,
        "closed": custsC
    }
    
    return JsonResponse(custslist)

@login_required(login_url='login')
def customerLoc(request):
    custs = Customer.objects.all()

    custs1 = custs.filter(source='Blog').count()
    custs2 = custs.filter(source = 'Social media').count()
    custs3 = custs.filter(source= 'Friend').count()
    custs4 = custs.filter(source= 'Google search').count()
    custs5 = custs.filter(source = 'Product package').count()
    custs6 = custs.filter(source= 'Company Employee').count()

    custslocation={
        "location1": custs1,
        "location2": custs2,
        "location3": custs3,
        "location4": custs4,
        "location5": custs5,
        "location6": custs6
    }
    
    return JsonResponse(custslocation)