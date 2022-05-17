from django.contrib.auth.backends import BaseBackend
from todo_api.models import User


class AuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # TODO: password hash encode
            user = User.objects.get(username=username, password=password)
            return user
        except User.DoesNotExist:
            return None