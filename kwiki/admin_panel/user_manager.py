from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.backends import ModelBackend
from .models import User
import requests


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given email, password and username.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(username, email, password, **extra_fields)

    def get_or_create(self, username, **extra_fields):
        user = User.objects.values().get(username=username)
        if user is not None:
            return user
        else:
            self.create_user(self, username=username)


class CustomAuth(ModelBackend):
    """Log in to Django without providing a password.

    """
    def authenticate(self, username=None, password=None):
        if requests.post('http://95.213.128.80:8080/auth',
                         data={'login': username, 'password': password}):
            try:
                return User.objects.get(username=username)
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
