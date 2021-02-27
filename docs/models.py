from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from projects import models as ProjectID
from tasks import models as TaskID
from reports import models as ReportID

class Doc(models.Model):
    KIND_CHOICE =(
        ('General', 'General'),
        ('Audit', 'Audit'),
        ('Project Related', 'Project Related'),
        ('Policy', 'Policy'),
        ('Procedures', 'Procedures '),
        ('Guidelines', 'Guidelines'),
        ('Forms and templates', 'Forms and templates'),
        ('Minutes', 'Minutes'),
    )

    name = models.CharField(max_length=250, null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.NOT_PROVIDED)
    projectID = models.ForeignKey(ProjectID.Project, null=True, blank=True, on_delete=models.SET_NULL)
    taskID = models.ForeignKey(TaskID.Task, null=True, blank=True, on_delete=models.SET_NULL)
    reportID = models.ForeignKey(ReportID.Report, null=True, blank=True, on_delete=models.SET_NULL) 
    classified = models.BooleanField(default = False)
    document = models.FileField(null=False, blank=False)
    kind = models.CharField(choices=KIND_CHOICE, max_length=30, null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(null=True, blank=True)
    dateDeleted = models.DateTimeField(null=True, blank=True)

    def __str__ (self):
        return self.name
