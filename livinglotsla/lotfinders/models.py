from django.db import models
from django.utils.translation import ugettext_lazy as _


class LotFinderAttempt(models.Model):

    checked = models.DateTimeField(_('checked'), auto_now=True)

    STATUS_CHOICES = (
        ('added', 'added'),
        ('not added', 'not added'),
    )
    status = models.CharField(
        _('status'),
        max_length=50,
        choices=STATUS_CHOICES,
        default='not added'
    )

    reason = models.TextField(
        _('reason'),
        blank=True,
        null=True
    )

    parcel = models.ForeignKey(
        'parcels.Parcel',
        blank=True,
        null=True
    )
