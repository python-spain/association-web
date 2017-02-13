# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "created_at", "modified_at", "created_by",)
    list_display_links = list_display

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user

        return super().save_model(request, obj, form, change)


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "created_at", "modified_at", "created_by",)
    list_display_links = list_display

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user

        return super().save_model(request, obj, form, change)


class FaqEntryAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at", "modified_at", "created_by",)
    list_display_links = list_display

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user

        return super().save_model(request, obj, form, change)


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("description", "created_at", "modified_at", "created_by",)
    list_display_links = list_display

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user

        return super().save_model(request, obj, form, change)


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Page, PageAdmin)
admin.site.register(models.FaqEntry, FaqEntryAdmin)
admin.site.register(models.Attachment, AttachmentAdmin)
