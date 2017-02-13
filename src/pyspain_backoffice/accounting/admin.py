# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("identifier", "attachment", "date",)
    list_display_links = list_display
    list_filter = ("date",)
    date_hierarchy = "date"


class AccountAdmin(admin.ModelAdmin):
    list_display = ("identifier", "name", "created_at",)
    list_display_links = list_display


class RegisterAdmin(admin.ModelAdmin):
    list_display = ("account", "date", "subject", "debit", "credit",)
    list_display_links = list_display
    list_filter = ("date",)
    date_hierarchy = "date"


class RegisterInline(admin.TabularInline):
    model = models.Register
    extra = 0
    max_num = 100


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("uuid", "fiscal_year", "created_at",)
    list_display_links = list_display
    list_filter = ("fiscal_year__name",)

    inlines = [RegisterInline]


class FiscalYearAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at",)
    list_display_links = list_display


admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
admin.site.register(models.Register, RegisterAdmin)
admin.site.register(models.FiscalYear, FiscalYearAdmin)
