"""
#This system is made by Abd-el-Rahman Mohammed Mohammed Abd-ell-Gabbar
#TP: TP049556

ManageLite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from acc.views import home, prefChart, loginPage, logoutSite, userPage, perPersonChart, riskPer, customerPer, customerLoc
from projects.views import projectCreate, projectUpdate, projectView, projectDelete
from risks.views import riskreg, riskUpdate, riskDelete
from tasks.views import taskCreate, taskUpdate, taskView, taskDelete
from reports.views import auditboard, reportCreate, reportUpdate, reportView, reportDelete
from docs.views import completeDelete, docboard, docAdminCreate, docDelete, edocDelete, docEmployeeCreate, edocboard
from custs.views import customerDelete, customerUpdate, customerForm, customerComplaints
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name= "admin"),
    path('user/', userPage, name= "user"),
    path('', home, name= "home"),
    path('completedelete/', completeDelete, name= "completeDelete"),
    path('docboard/', docboard, name= "docboard"),
    path('docadmincreate/', docAdminCreate, name= "docAdminCreate"),
    path('edocdelete/<str:pk>/', edocDelete, name= "edocDelete"),
    path('edocboard/', edocboard, name= "edocboard"),
    path('docemployeecreate/', docEmployeeCreate, name= "docEmployeeCreate"),
    path('docdelete/<str:pk>/', docDelete, name= "docDelete"),
    path('projectcreate/', projectCreate, name= "projectCreate"),
    path('projectupdate/<str:pk>/', projectUpdate, name= "projectUpdate"),
    path('projectview/<str:pk>/', projectView, name= "projectView"),
    path('projectDelete/<str:pk>/', projectDelete, name= "projectDelete"),
    path('taskcreate/', taskCreate, name= "taskCreate"),
    path('taskupdate/<str:pk>/', taskUpdate, name= "taskUpdate"),
    path('taskview/<str:pk>/', taskView, name= "taskView"),
    path('taskdelete/<str:pk>/', taskDelete, name= "taskDelete"),
    path('auditboard/', auditboard, name= "auditboard"),
    path('reportcreate/', reportCreate, name= "reportCreate"),
    path('reportupdate/<str:pk>/', reportUpdate, name= "reportUpdate"),
    path('reportview/<str:pk>/', reportView, name= "reportView"),
    path('reportdelete/<str:pk>/', reportDelete, name= "reportDelete"),
    path('customercomplaints/', customerComplaints, name= "customerComplaints"),
    path('customerform/', customerForm, name= "cust_form"),
    path('customerdelete/<str:pk>/', customerDelete, name= "customerDelete"),
    path('customerupdate/<str:pk>/', customerUpdate, name= "customerUpdate"),
    path('riskregister/', riskreg, name= "risk"),
    path('risk_update/<str:pk>/', riskUpdate, name= "risku"),
    path('risk_delete/<str:pk>/', riskDelete, name= "riskd"),
    path('login/', loginPage, name= "login"),
    path('logout/', logoutSite, name= "logout"),
    path('prefChart/', prefChart, name= "prefChart"),
    path('riskPer/', riskPer, name= "riskPer"),
    path('customerPer/', customerPer, name= "customerPer"),
    path('perPersonChart/', perPersonChart, name= "perPersonChart"),
    path('customerLoc/', customerLoc, name= "customerLoc"),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = 'QMS Admin Page'
admin.site.site_title = 'Admin Page'