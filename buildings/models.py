from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    level = models.IntegerField(default=1)
    
    cost_in_egg_bool = models.BooleanField(default=False)
    cost = models.FloatField(default=0)
    cost_in_egg = models.FloatField(default=0)

    income_per_second_in_egg_bool = models.BooleanField(default=False)
    income_per_second = models.FloatField(default=0)
    income_per_second_in_egg = models.FloatField(default=0)
    
    income_per_click_in_egg_bool = models.BooleanField(default=False)
    income_per_click = models.FloatField(default=0)
    income_per_click_in_egg = models.FloatField(default=0)
    
    owned = models.BooleanField(default=False)

    def __str__(self):
        return self.name
