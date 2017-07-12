from django.db import models

# Create your models here.


class Article(models.Model):
    catalog = models.ForeignKey('Catalog', verbose_name='Каталог')
    title = models.CharField(verbose_name='Название', max_length=200)
    article_text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата')
    is_index = models.BooleanField(verbose_name='Индексная?')

    def __str__(self):
        return str(self.catalog) + ' --> ' + self.title


class Catalog(models.Model):
    parent_catalog = models.ForeignKey('Catalog', verbose_name='Родительский каталог',
                                       default='/', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return str(self.parent_catalog) + ' --> ' + self.title
