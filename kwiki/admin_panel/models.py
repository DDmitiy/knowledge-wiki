from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group, Permission, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .user_manager import UserManager

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

class User(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(Group, 'Группы', blank=True)
    user_permissions = models.ManyToManyField(Permission, 'Права', blank=True)
    is_superuser = models.BooleanField('Суперпользователь?', default=False)
    karma = models.IntegerField('Карма', default=0)
    is_staff = models.BooleanField('Персонал?', default=False)
    is_active = models.BooleanField('Активный?', default=True)
    username = models.CharField('Логин', max_length=30, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    # fields, which must be prompted when creating user via the `createsuperuser`
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username
