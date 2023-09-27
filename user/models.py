from django.contrib.auth.models import User
from django.db import models
from buildings.models import Building
from django.contrib.postgres.fields import ArrayField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buildings = models.ManyToManyField(Building, related_name='user_profiles')
    buildings_level = models.ManyToManyField(Building, through='BuildingLevel', related_name='user_profile_levels_new')
    money = models.IntegerField(default=0)
    Egg = models.IntegerField(default=0)
    Hay = models.IntegerField(default=0)
    egg_per_second = models.IntegerField(default=0)
    money_per_second = models.IntegerField(default=0)
    int_array = models.CharField(max_length=255, null=True, blank=True)

    def update_int_array(self, new_value):
        if self.int_array is None or self.int_array == '':
            self.int_array = str(new_value)
        else:
            int_list = [int(x) for x in str(self.int_array).split(',') if x]
            int_list.append(new_value)
            self.int_array = ','.join(str(x) for x in int_list)
            

    def __str__(self):
        return self.user.username

class BuildingLevel(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    egg_in_storage = models.IntegerField(default=0)