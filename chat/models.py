from django.db import models
from django.contrib.auth.models import User ##

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    #manytomany relacion Sala a multiples Usuario y Usuario a multiples salas
    users = models.ManyToManyField(User, related_name='rooms_joined', blank =True)
    
    def __str__(self):
        return self.name

    