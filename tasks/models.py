from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from projects import models as PName

class Task(models.Model):
    
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.NOT_PROVIDED)
    project = models.ForeignKey(PName.Project, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=250, null=False)
    description = models.TextField(null=False)
    deadline = models.DateTimeField(null=True, blank=True)
    finished = models.BooleanField(default=False)
    team = models.ManyToManyField(User, related_name='tTeam')
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)
    dateFinished = models.DateTimeField(null=True, blank=True)

    def __str__ (self):
        return self.title