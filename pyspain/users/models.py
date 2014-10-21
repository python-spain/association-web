# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin,
                                        BaseUserManager)
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    The user manager class. Overwrite the default django user manager to use email instead the
    username.
    """
    def create_user(self, email, password='', **kwargs):
        if not email:
            raise ValueError(_("Users must have an email address"))

        user = self.model(email=self.normalize_email(email), **kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        if not email:
            raise ValueError(_("Users must have an email address"))

        user = self.model(email=self.normalize_email(email), **kwargs)

        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):
    """
    The user model class. Overwrite the default django user model to use email instead the
    username and add some new fields to define the diferent types of user will be.
    """
    email = models.EmailField(null=False, blank=False, unique=True,
                              verbose_name=_(u"email"))
    first_name = models.CharField(max_length=256, null=True, blank=True,
                                  verbose_name=_(u"nombre"))
    last_name = models.CharField(max_length=256, null=True, blank=True,
                                 verbose_name=_(u"apellidos"))

    is_staff = models.BooleanField(
        default=False, verbose_name=_(u"es staff"),
        help_text=_("Designates whether the user can log into this admin site."))
    is_active = models.BooleanField(
        default=True, verbose_name=_(u"está activado"),
        help_text=_("Designates whether this user should be treated as "
                    "active. Unselect this instead of deleting accounts."))

    date_joined = models.DateTimeField(default=timezone.now(),
                                       verbose_name=_(u"fecha de registro"))

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        ordering = ("first_name", "last_name", "email")
        verbose_name = _(u'user')
        verbose_name_plural = _(u'users')

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "first_name__icontains", "last_name__icontains", "email__icontains")

    @property
    def has_password(self):
        if (not self.password) or self.password == u'!':
            return False
        return True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between or the email.

        :return: the full name.
        :rtype: string.
        """
        if self.first_name:
            return "{0} {1}".format(self.first_name.strip(),
                                    self.last_name.strip())
        return self.email

    def get_short_name(self):
        """
        Returns the first name for the user or the email.

        :return: the first name or the email.
        :rtype: string
        """
        return self.first_name or self.email
