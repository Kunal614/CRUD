from django.db import models

# Create your models here.



class user(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    Class = models.CharField(default=None , max_length=50)
    Comments = models.CharField(max_length=200 , default=None)