from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from rest_framework.authtoken.models import Token


# Create your models here.

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        user = super().create_user(username, email, password, **extra_fields)
        token = Token.objects.create(user=user)
        token.save()
        user.token = token.key
        user.save()

        return user


class User(AbstractUser):
    token = models.CharField(max_length=64, null=True)
    objects = CustomUserManager()

    class Meta(AbstractUser.Meta):
        pass
