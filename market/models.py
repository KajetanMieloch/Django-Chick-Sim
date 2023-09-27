from django.db import models


class Shopping_item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    costbuy = models.FloatField(default=0)
    costsell = models.FloatField(default=0)
    
    def __str__(self):
        return self.name