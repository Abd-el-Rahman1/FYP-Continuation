from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from risks.models import Risk
from projects.models import Project
from reports.models import Report
from tasks.models import Task
from custs.models import Customer
from docs.models import Doc

class DocCForm(ModelForm):
    class Meta:
        model = Doc
        fields = '__all__'
        exclude = ('creator',)


class CustCForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class RiskCForm(ModelForm):
    class Meta:
        model = Risk
        fields = '__all__'

class ProjectCForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ('creator',)

class ReportCForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ('creator',)

class TaskCForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('creator',)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email' , 'password1', 'password2', 'groups']
