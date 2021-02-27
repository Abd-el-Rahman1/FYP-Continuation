from django.db import models

from pms import models as ManagerID
from emps import models as EmpID
from django.contrib.auth.models import User
from projects import models as PName

# Create your models here.
class Risk(models.Model):

    STATUS_CHOICE =(
        ('Open', 'Open'),
        ('Inprogress', 'Inprogress'),
        ('Closed', 'Closed'),
    )
    PRIORITY_CHOICE =(
        ('Very High', 'Very High'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Very Low', 'Very Low'),
    )

    title = models.CharField(max_length=250, null=False)
    description = models.TextField(max_length=1000, null=False)
    category = models.CharField(max_length=150, blank=True, null=False)
    probability = models.DecimalField(decimal_places=1, max_digits=2)
    impact = models.DecimalField(decimal_places=1, max_digits=2)
    priority = models.CharField(choices=PRIORITY_CHOICE, max_length=30, null=True)
    effect = models.TextField(max_length=1000, blank=True, null=False)
    owner = models.ManyToManyField(User)
    pName = models.ForeignKey(PName.Project, null=True, blank=True, on_delete=models.SET_NULL)
    rrp = models.TextField(max_length=1000, blank=True, null=False)
    status = models.CharField(choices=STATUS_CHOICE, max_length=30, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(null=True, blank=True)
    dateFinished = models.DateTimeField(null=True, blank=True)


    def __str__ (self):
        return self.title