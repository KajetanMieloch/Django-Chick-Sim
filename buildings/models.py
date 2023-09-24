from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cost = models.IntegerField(default=0)
    owned = models.BooleanField(default=False)

    def __str__(self):
        return self.name
