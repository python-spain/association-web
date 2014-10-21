# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.db import models
from django.utils import timezone


class Member(models.Model):
    full_name = models.CharField(max_length=500,
                                 verbose_name=_("Nombre completo"))

    identity_number = models.CharField(
                        verbose_name=_("Numero de identidad (DNI/NIE)"),
                        max_length=50)

    joined_at = models.DateField(
                    verbose_name=_("Se ha unido en"),
                    default=lambda: timezone.now().date())

    phone = models.CharField(max_length=200,
                             verbose_name=_("Telefono/s"))
    email = models.EmailField(max_length=200,
                              verbose_name=_("Email"))

    address = models.TextField(max_length=200,
                               verbose_name=_("Direccion postal"))

    board_of_trustees = models.BooleanField(
                            verbose_name=_("Miembro de junta directiva"),
                            default=False)

    user = models.ForeignKey("users.User", null=True, blank=True,
                             default=None, verbose_name=_("Usuario asociado"))

    # Optional social data. Should used make
    # a public members list.
    twitter_username = models.CharField(max_length=255, blank=True, default="",
                                        verbose_name=_("Usuario de twitter"))

    github_username = models.CharField(max_length=255, blank=True, default="",
                                       verbose_name=_("Usuario de github"))

    webpage_url = models.URLField(max_length=255, blank=True,
                                  verbose_name=_("Web/Blog"))

    internal_account_number = models.CharField(max_length=100, blank=True, default="",
                                               verbose_name=_("Numero de cuenta interno"))

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ["full_name"]
        verbose_name = _("Miembro")


class MemberPayment(models.Model):
    """
    Register of memebers payment.
    """

    TYPE_WIRE_TRANSFER = 0
    TYPE_CASH_PAYMENT = 1

    TYPE_CHOICES = ((TYPE_WIRE_TRANSFER, _("Transferencia bancaria")),
                    (TYPE_CASH_PAYMENT, _("Pago al contado")),)

    member = models.ForeignKey("Member", related_name="payment_registers",
                               verbose_name=_("Miembro"))
    payment_date = models.DateField(_("Fecha de pago"),
                                    default=lambda: timezone.now().date())
    quantity = models.DecimalField(max_digits=5, decimal_places=1,
                                   verbose_name=_("Cantidad abonada"))
    payment_type = models.IntegerField(choices=TYPE_CHOICES)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = _("Registo de pagos")
        verbose_name_plural = _("Registros de pagos")

    def __str__(self):
        return ugettext("Registo de pago {0}").format(self.id)


class Attachment(models.Model):
    """
    Member attachement class. Serves for store documentatation associated
    with a member, such as identity document, payments, etc....
    """

    TYPE_IDCARD = 0
    TYPE_PAYMENT = 1
    TYPE_OTHER = 1000

    TYPE_CHOICES = ((TYPE_IDCARD, _("Documento de identidad")),
                    (TYPE_PAYMENT, _("Justificante de pago")),
                    (TYPE_OTHER, _("Otros")),)

    member = models.ForeignKey("Member", related_name="attachments")
    file = models.FileField(upload_to="member/attachments/")
    type = models.IntegerField(choices=TYPE_CHOICES)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(editable=False, auto_now=True)
