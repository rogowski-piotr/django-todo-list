from hashlib import new
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(blank = False, unique=True, max_length = 255)
    password = models.CharField(blank = True, max_length = 255)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Todo(models.Model):
    title = models.CharField(max_length = 50, blank=False)
    content = models.CharField(max_length = 200, blank=False)
    completed = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.task