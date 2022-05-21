from django.contrib.auth.backends import BaseBackend
from todo_api.models import User
import hashlib


class AuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            passwordHash = hashlib.md5(str(password).encode())
            user = User.objects.get(username=username, password=passwordHash.hexdigest())
            return user
        except User.DoesNotExist:
            return None