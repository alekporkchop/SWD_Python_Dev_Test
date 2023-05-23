from django.db import models
from datetime import datetime

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    
