"""
Database models.
"""
from core.managers import UserManager
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_active = models.DateTimeField(_('last_active'), null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Company(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Recruiter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='recruiter', null=True, blank=True,
                                on_delete=models.CASCADE)
    company = models.ForeignKey(Company, default=None, null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='recruiters')
    is_admin = models.BooleanField(default=False)
