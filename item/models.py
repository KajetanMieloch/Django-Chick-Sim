from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='department_images')
    
    class Meta:
        verbose_name = 'Department'

    def __str__(self):
        return self.name

class Chicken(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_bought = models.BooleanField(default=False)
    image = models.ImageField(upload_to='chicken_images')

    class Meta:
        verbose_name = 'Chicken'

    def __str__(self):
        return self.name