import requests
from django.contrib.auth.backends import ModelBackend

from .models import User


class CustomAuth(ModelBackend):
    """Log in to Django without providing a password.

    """
    def authenticate(self, username=None, password=None):
        if requests.post('http://95.213.128.80:8080/auth',
                         data={'login': username, 'password': password}):
            try:
                user = User.objects.get(username=username)
                return user
            except User.DoesNotExist:
                User.objects.create_user(username=username)
                return User.objects.get(username=username)
        else:
            return None

    def get_user(self, user_id):

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None