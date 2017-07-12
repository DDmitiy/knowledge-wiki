from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Article(models.Model):
    catalog = models.ForeignKey('Catalog', verbose_name='Каталог')
    title = models.CharField(verbose_name='Название', max_length=200)
    article_text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата')
    is_index = models.BooleanField(verbose_name='Индексная?')

    def clean(self):
        if self.is_index and Article.objects.filter(catalog=self.catalog, is_index=True).exclude(id=self.id).exists():
            raise ValidationError('This catalog have index page yet')

    def __str__(self):
        return self.title


class Catalog(models.Model):
    parent_catalog = models.ForeignKey('Catalog', verbose_name='Родительский каталог', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return '{} --> {}'.format(str(self.parent_catalog), self.title)
