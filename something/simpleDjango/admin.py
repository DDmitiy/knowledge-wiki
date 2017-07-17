from django.contrib import admin
from .models import Article, Catalog, User
# Register your models here.


class ArticleLook(admin.ModelAdmin):
    list_display = ('title', 'catalog', 'date', 'is_index')
    list_filter = ['catalog', 'date', 'is_index']


class CatalogLook(admin.ModelAdmin):
    list_display = ('title', 'parent_catalog')
    list_filter = ['parent_catalog']


admin.site.register(Article, ArticleLook)
admin.site.register(Catalog, CatalogLook)
admin.site.register(User)