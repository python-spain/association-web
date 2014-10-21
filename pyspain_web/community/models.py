# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Community(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)

    created_by = models.ForeignKey("users.User", null=True, blank=True, related_name="+",
                                   default=None, verbose_name=_("Creado por"))

class Event(models.Model):
    name = models.CharField(max_length=500)
    link = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=255)

    description = models.TextField(blank=True)

    community = models.ForeignKey("Community", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)

    created_by = models.ForeignKey("users.User", null=True, blank=True, related_name="+",
                                   default=None, verbose_name=_("Creado por"))

# class JobOffer(models.Model):
#     title = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     company_webpage = models.URLField(max_length=500, blank=True)
#
#     is_active = models.BooleanField(default=False)
#     expires_at = models.DateField(null=True, default=None, blank=True)
#
#     description = models.TextField()
#     external_link = models.URLField(max_length=500)
