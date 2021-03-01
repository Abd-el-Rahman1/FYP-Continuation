from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
import datetime
from .models import Risk
from projects.models import Project
from points.models import Point
from acc.filters import RiskFilter
from acc.forms import RiskCForm, CreateUserForm
from acc.decorators import unauthenticated_user, allowed_users, admin_only

#Risk register view for search creation and status.
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def riskreg(request):
    risks = Risk.objects.all()
    #filtering
    O_risks = risks.filter(status='Open').count() + risks.filter(status = 'Inprogress').count()
    C_risks = risks.filter(status='Closed').count()
    total_risks = risks.count()
    #search
    myFilter = RiskFilter(request.GET, queryset=risks)
    risks = myFilter.qs
    #creation
    form = RiskCForm()
    if request.method == 'POST':
        form = RiskCForm(request.POST)
        if form.is_valid():
            Point.objects.create(pointOwner=request.user, dateCreated=datetime.datetime.now())
            form.save()
            return redirect('risk')

    return render(request, 'riskRegister.html',{
    'form': form,
    'risks':risks,
    'O_risks': O_risks,
    'C_risks': C_risks,
    'total_risks': total_risks,
    'myFilter':myFilter

    })


@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
def riskDelete(request, pk):
    risks = Risk.objects.get(id=pk)

    if request.method == 'POST':
        risks.delete()
        return redirect('risk')

    risks = {'risks':risks}
    return render(request, 'risk_delete.html', risks)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Audit'])
def riskUpdate(request, pk):
    risks = Risk.objects.get(id=pk)
    form = RiskCForm(instance=risks)
    if request.method == 'POST':
        form = RiskCForm(request.POST, instance=risks)
        if form.is_valid():
            risks.dateUpdated = datetime.datetime.now()
            if risks.status == 'Closed':
                risks.dateFinished = datetime.datetime.now()
            form.save()
            return redirect('risk')

    form = {'form':form}
    return render(request, 'risk_update.html', form)