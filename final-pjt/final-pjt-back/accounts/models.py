from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)
    user_image = models.CharField(max_length=500)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')