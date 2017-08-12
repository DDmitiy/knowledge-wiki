from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, UserManager, PermissionsMixin
from django.core.mail import send_mail
from django.utils import timezone


# Create your models here.


class Article(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    catalog = models.ForeignKey('Catalog', verbose_name='Каталог')
    title = models.CharField('Название', max_length=200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)
    is_index = models.BooleanField('Индесная ?')

    def clean(self):
        if self.is_index and Article.objects.filter(catalog=self.catalog, is_index=True).exclude(id=self.id).exists():
            raise ValidationError('Этот каталок уже имеет индексную страницу')

    def __str__(self):
        return self.title


class Catalog(models.Model):
    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    parent_catalog = models.ForeignKey('Catalog', verbose_name='Родительский каталог', blank=True, null=True)
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return '{0} --> {1}'.format(self.parent_catalog, self.title)


class CustomUser(models.Model):
    # birth_date = models.DateField('Дата рождения', blank=True, null=True)
    groups = models.ManyToManyField(Group, 'Группы', blank=True)
    user_permissions = models.ManyToManyField(Permission, 'Права', blank=True)
    is_superuser = models.BooleanField('Суперпользователь?')
    karma = models.IntegerField('Карма', default=0)
    is_staff = models.BooleanField('Персонал?')
    email = models.EmailField('E-mail', unique=True)
    first_name = models.CharField('Имя', max_length=30, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True, null=True)
    username = models.CharField('Логин', max_length=30, unique=True)
    password = models.CharField('Пароль', max_length=100)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#
#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '{0} {1}'.format(self.first_name, self.last_name)
#         return full_name.strip()
#
#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name
#
#     def email_user(self, subject, message, from_email=None, **kwargs):
#         '''
#         Sends an email to this User.
#         '''
#         send_mail(subject, message, from_email, [self.email], **kwargs)
