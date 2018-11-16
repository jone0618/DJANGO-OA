from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=13,
        verbose_name='手机号'
    )
    age = models.IntegerField(
        verbose_name='年纪',
        null=True
    )
