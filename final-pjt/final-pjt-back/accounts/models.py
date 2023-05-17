from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20)
    user_image = models.ImageField(blank=True, null=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')