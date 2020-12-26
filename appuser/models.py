from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class State(models.Model):
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

class City(models.Model):
    city_state = models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class Area(models.Model):
    area_city = models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    area_name = models.CharField(max_length=50)

    def __str__(self):
        return self.area_name

class OWNUSER(AbstractUser):
    mobile_no = models.CharField(blank = False, max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    state = models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,null=True)
