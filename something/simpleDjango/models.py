from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, UserManager

# Create your models here.


class Article(models.Model):
    catalog = models.ForeignKey('Catalog', verbose_name=_('catalog'))
    title = models.CharField(_('title'), max_length=200)
    article_text = models.TextField(_('article text'))
    date = models.DateTimeField(_('date'))
    is_index = models.BooleanField(_('home page?'))

    def clean(self):
        if self.is_index and Article.objects.filter(catalog=self.catalog, is_index=True).exclude(id=self.id).exists():
            raise ValidationError('This catalog have index page yet')

    def __str__(self):
        return self.title


class Catalog(models.Model):
    parent_catalog = models.ForeignKey('Catalog', verbose_name=_('catalog'), blank=True, null=True)
    title = models.CharField(_('title'), max_length=200)

    def __str__(self):
        return '{0} --> {1}'.format(self.parent_catalog, self.title)


class User(AbstractBaseUser):
    birth_date = models.DateField(_('birthday'))
    groups = models.ManyToManyField(Group, _('group'))
    user_permissions = models.ManyToManyField(Permission, _('permissions'))
    is_superuser = models.BooleanField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
