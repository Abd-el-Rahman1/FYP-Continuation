from django.db import models

# Create your models here.

class Manager(models.Model):
    SOURCE_CHOICES =(
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Software Dev', 'Software Dev'),
        ('Human Resources', 'Human Resources'),
        ('Scrum Master', 'Scrum Master'),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    status = models.BooleanField(default=True)
    role = models.CharField(choices=SOURCE_CHOICES, max_length=250, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.name