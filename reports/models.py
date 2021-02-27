from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
 
class Report(models.Model):
    STATUS_CHOICE =(
    ('NCR', 'NCR'),
    ('OFI', 'OFI'),
    )

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.NOT_PROVIDED)
    auditee = models.ManyToManyField(User, related_name='auditees')
    location = models.CharField(max_length=250, blank=False, null=False)
    areaAudited = models.TextField(blank=False, null=False)
    NCR_or_OFI = models.CharField(choices=STATUS_CHOICE, max_length=30, null=False, blank=False)
    comment = models.TextField(blank=True, null=True)
    closed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)   
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)
    dateFinished = models.DateTimeField(null=True, blank=True)

    def id (self):
        return self.id


