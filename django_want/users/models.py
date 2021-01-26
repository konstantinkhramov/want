from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    token = models.CharField(max_length=64, null=True)

    class Meta(AbstractUser.Meta):
        pass
