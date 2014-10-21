# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


class CommunityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "slug", "created_at", "modified_at", "created_by",)
    list_display_links = list_display


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "slug", "created_at", "modified_at", "created_by",)
    list_display_links = list_display


admin.site.register(models.Community, CommunityAdmin)
admin.site.register(models.Event, EventAdmin)
