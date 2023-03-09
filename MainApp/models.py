from django.db import models
from django.contrib.auth.models import AbstractUser


class UserData(AbstractUser):
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Notes(models.Model):
    author = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=40, blank=False)
    description = models.TextField(blank=False)
