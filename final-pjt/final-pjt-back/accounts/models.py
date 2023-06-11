from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    point = models.IntegerField(default=0)
    userImg = models.ImageField(upload_to='users' ,null=True)


    