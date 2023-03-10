from __future__ import annotations

from django.core.exceptions import ValidationError
from django.db import models

from .choosen import PAY_STATUS
from .choosen import PAY_TYPE
from apps.common.models import BaseModel


class Payment(BaseModel):
    user = models.ForeignKey(
        'accounts.Account', on_delete=models.CASCADE, verbose_name='User',
    )
    course = models.ForeignKey(
        'courses.Course', on_delete=models.CASCADE, verbose_name='Course',
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Price',
    )
    payment_type = models.CharField(
        max_length=255, choices=PAY_TYPE, verbose_name='Payment Type',
    )
    payment_status = models.CharField(
        max_length=255, choices=PAY_STATUS, verbose_name='Payment Status',
    )

    def clean(self):
        if self.payment_status == 'Failed' and self.payment_type == 'Click':
            raise ValidationError('You can not pay for free course')

        # TODO: check if user has already paid for this course

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.user.username
