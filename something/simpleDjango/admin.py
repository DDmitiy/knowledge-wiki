from django.contrib import admin
from .models import Article, Catalog
# Register your models here.


class ArticleLook(admin.ModelAdmin):
    list_display = ('title', 'catalog', 'date')
    list_filter = ['catalog', 'date']


class CatalogLook(admin.ModelAdmin):
    list_display = ('title', 'parent_catalog')
    list_filter = ['parent_catalog']


admin.site.register(Article, ArticleLook)
admin.site.register(Catalog, CatalogLook)