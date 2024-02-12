from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.IntegerField(default=0)
    def __str__(self):
        return self.age 

class StreamPlatform(models.Model):
    name  = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name
    
# Create your models here
class WatchList(models.Model):
    title = models.CharField(max_length=40)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ManyToManyField(StreamPlatform)


    def __str__(self):
        return self.title
    
