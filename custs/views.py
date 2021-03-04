from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from points.models import Point
from .models import Customer
from acc.forms import CustCForm
from acc.decorators import unauthenticated_user, allowed_users, admin_only

@login_required(login_url='login')
def customerForm(request):
    custs = Customer.objects.all()
    form = CustCForm()
    if request.method == 'POST':
        form = CustCForm(request.POST)
        if form.is_valid():
            custs = form.save(commit=False)
            custs.status = 'Open'
            form.save()
            return redirect('http://www.apu.edu.my/')

    return render(request, 'customer_form.html', {'custs': custs, 'form': form,})

@login_required(login_url='login')
def customerComplaints(request):
    custs = Customer.objects.all()
    return render(request, 'customer_complaints.html', {'custs': custs})

@login_required(login_url='login')
def customerUpdate(request, pk):
    custs = Customer.objects.get(id=pk)
    form = CustCForm(instance=custs)
    if request.method == 'POST':
        form = CustCForm(request.POST, instance=custs)
        if form.is_valid():
            custs.dateUpdated = datetime.datetime.now()
            if custs.status == 'Closed':
                custs.dateFinished = datetime.datetime.now()             
            form.save()
            return redirect('customerComplaints')

    form = {'form':form}
    return render(request, 'customer_update.html', form)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
def customerDelete(request, pk):
    custs = Customer.objects.get(id=pk)
    if request.method == 'POST':
        custs.delete()
        return redirect('customerComplaints')

    custs = {'custs':custs}
    return render(request, 'customer_delete.html', custs)