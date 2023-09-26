from django.contrib.auth.models import User
from django.db import models
from buildings.models import Building

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buildings = models.ManyToManyField(Building, related_name='user_profiles')
    buildings_level = models.ManyToManyField(Building, through='BuildingLevel', related_name='user_profile_levels_new')
    money = models.IntegerField(default=0)
    egg = models.IntegerField(default=0)
    egg_per_second = models.IntegerField(default=0)
    money_per_second = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class BuildingLevel(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    egg_in_storage = models.IntegerField(default=0)