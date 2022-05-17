from hashlib import new
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(blank = False, unique=True, max_length = 255)
    password = models.CharField(blank = True, max_length = 255)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Todo(models.Model):
    task = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task