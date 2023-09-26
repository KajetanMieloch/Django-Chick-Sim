from django.db import models
from celery import shared_task
from datetime import timedelta
from django.utils import timezone

class Building(models.Model):
    
    id = models.IntegerField(primary_key=True)
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    level = models.IntegerField(default=1)
    
    cost = models.FloatField(default=0)

    eggs_per_click = models.FloatField(default=0)
    
    egg_capacity = models.IntegerField(default=0)
    
    owned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

