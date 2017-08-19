from django.contrib import admin
from .models import Article, Catalog, User
from django.forms.widgets import HiddenInput
# Register your models here.


class ArticleLook(admin.ModelAdmin):
    list_display = ('title', 'catalog', 'pub_date', 'is_index')
    list_filter = ['catalog', 'pub_date', 'is_index']


class CatalogLook(admin.ModelAdmin):
    list_display = ('title', 'parent_catalog')
    list_filter = ['parent_catalog']


class UserLook(admin.ModelAdmin):
    list_display = ('username', 'is_staff')
    list_filter = ['is_staff', 'is_superuser', 'groups']
    fieldsets = (
        (None, {'fields': ('username', 'is_staff', 'is_superuser', 'is_active')}),
        ('Groups & permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions')}),
        ('Advanced options', {
         'classes': ('collapse',),
         'fields': ('karma',)}),
    )


admin.site.register(User, UserLook)
admin.site.register(Article, ArticleLook)
admin.site.register(Catalog, CatalogLook)
# admin.site.register(CustomUser, UserLook)
