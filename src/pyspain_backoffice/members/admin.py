# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models


class PaymentInline(admin.TabularInline):
    model = models.MemberPayment
    extra = 0
    readonly_fields = ('id',)
    fields = ('id', 'quantity', 'payment_date',)


class MemberAdmin(admin.ModelAdmin):
    actions_on_top = True

    list_display = ('full_name', 'email', 'phone',
                    'joined_at', 'internal_account_number',)

    list_display_links = list_display
    search_fields = ["full_name", "email", "phone", "identity_number"]
    date_hierarchy = 'joined_at'

    inlines = [PaymentInline]

    fieldsets = (
        (None, {
            'fields': (
                ('full_name', 'identity_number'),
                ('email', 'phone'),
                ('address',),
            )
        }),
        ("Fechas", {
            'fields': ('joined_at',),
        }),
        ("Social", {
            'fields': ('twitter_username',
                       'github_username',
                       'webpage_url'),
        }),
        ("Metadatos", {
            'classes': ('collapse',),
            'fields': ('user', 'board_of_trustees',
                       'internal_account_number',),
        }),
    )


class MemberPaymentAdmin(admin.ModelAdmin):
    list_display = ("member", "payment_date", "quantity")
    list_display_links = list_display
    search_fields = ["member__full_name", "member__email", "member__identity_number"]
    date_hierarchy = 'payment_date'
    list_filter = ["member",]


class MemberAttachmentAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "member", "created_at", "file")
    list_display_links = list_display
    search_fields = ["member__full_name", "member__email", "member__identity_number"]
    list_filter = ("type", "created_at",)


admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.MemberPayment, MemberPaymentAdmin)
admin.site.register(models.Attachment, MemberAttachmentAdmin)
