from django.db import models
from django.utils import timezone
import time
class Task(models.Model):
    task = models.CharField(max_length=30)
    desc = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task
    

        
