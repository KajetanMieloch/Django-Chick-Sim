from django.contrib.auth.models import User
from django.db import models
from buildings.models import Building

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField(default=0)
    buildings = models.ManyToManyField(Building)

    def __str__(self):
        return self.user.username