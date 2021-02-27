from django.db import models

# Create your models here.

class Customer(models.Model):
    SOURCE_CHOICES =(
        ('Blog', 'Blog'),
        ('Social media', 'Social media'),
        ('Friend', 'Friend'),
        ('Google search', 'Google search'),
        ('Product package', 'Product package'),
        ('Company Employee', 'Company Employee'),
    )

    STATUS_CHOICE =(
        ('Unopened', 'Unopened'),
        ('Inprogress', 'Inprogress'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField(default=0, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=250, null=True, blank=True)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=250, null=True, blank=True)
    problem = models.TextField(max_length=1000, null=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(null=True, blank=True)
    dateFinished = models.DateTimeField(null=True, blank=True)

    def __str__ (self):
        return self.name
