from django.db import models
from django.conf import settings


# Create your models here.
 
class Point(models.Model):
    
    pointOwner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_created=True)

    def User (self):
        return self.pointOwner