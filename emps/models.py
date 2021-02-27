from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    
    SOURCE_CHOICES =(
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Dev', 'Dev'),
        ('Customer Support', 'Customer Support'),
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    role = models.CharField(choices=SOURCE_CHOICES, max_length=250, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.name