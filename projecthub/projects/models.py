# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    PRIORITY_CHOICES = [(1, 'High'),(2, 'Medium'),(3, 'Low')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True)
    details = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_pinned = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=2)


    def __str__(self):
        return self.title


