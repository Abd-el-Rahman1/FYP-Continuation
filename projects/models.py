from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



# Create your models here.
 
class Project(models.Model):
    
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.NOT_PROVIDED)
    name = models.CharField(max_length=250, null=False)
    sponsors = models.CharField(max_length=250, blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    description = models.TextField(null=False)
    businessCase = models.TextField(blank=True, null=True)
    budget = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    finished = models.BooleanField(default=False)
    team = models.ManyToManyField(User, related_name='pTeam')
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)
    dateFinished = models.DateTimeField(null=True, blank=True)

    def __str__ (self):
        return self.name


