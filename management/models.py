from django.db import models
from django.conf import settings 
from django.contrib.auth import get_user_model

# Create your models here.

class clockIn(models.Model):
    teacher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"created on {self.created}"

class clockOut(models.Model):
    clock_in = models.OneToOneField(clockIn, on_delete=models.CASCADE)
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"updated on {self.created}"
