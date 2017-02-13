# -*- coding: utf-8 -*-

import uuid

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.db import models
from django.utils import timezone


class FiscalYear(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ["name", "created_at"]
        verbose_name = _("Año fiscal")
        verbose_name_plural = _("Años fiscales")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    uuid = models.CharField(max_length=36, unique=True, default=uuid.uuid1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    fiscal_year = models.ForeignKey("FiscalYear", related_name="transactions")

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Transaccion")
        verbose_name_plural = _("Transaccion")

    def __str__(self):
        return "Transaction: {0}".format(self.uuid)


class Invoice(models.Model):
    identifier = models.CharField(max_length=255,
                                  verbose_name=_("Numero de factura"))
    attachment = models.FileField(upload_to="invoices/%d/%Y",
                                  verbose_name=_("Factura en pdf"))
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["date", "identifier"]
        verbose_name = _("Factura")
        verbose_name_plural = _("Facturas")

    def __str__(self):
        return "Invoice: {0} ({1})".format(self.identifier, self.date)


class Account(models.Model):
    identifier = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ["identifier"]
        verbose_name = _("Cuenta")
        verbose_name_plural = _("Cuentas")

    def __str__(self):
        return "{0} - {1}".format(self.identifier, self.name)


class Register(models.Model):
    account = models.ForeignKey("Account", related_name="entries")

    invoice = models.ForeignKey("Invoice", related_name="registers",
                                verbose_name=_("Factura"),
                                null=True, blank=True, default=None)

    transaction = models.ForeignKey("Transaction", related_name="registers")

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    date = models.DateField(verbose_name=_("Fecha"), default=timezone.now)

    subject = models.CharField(max_length=200)
    debit = models.DecimalField(max_digits=16, decimal_places=4)
    credit = models.DecimalField(max_digits=16, decimal_places=4)

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Registro")
        verbose_name_plural = _("Registros")

    def __str__(self):
        return "Register: {0}".format(self.date)
