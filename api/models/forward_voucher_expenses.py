# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov
Forward voucher expenses / Дополнительные затраты экспедиторской расписки
"""

from django.db import models
from api.models.add_service import AdditionalService
from api.models.forward_voucher import ForwardVoucher

__author__ = 'ildyakov'


class ForwardVoucherExpenses(models.Model):
    """
    Forward expenses / Дополнительные затраты
    """

    """Forward voucher / Экспедиторская расписка"""
    forward_voucher = models.ForeignKey(ForwardVoucher, on_delete=models.CASCADE,)

    """Additional service / Дополнительная услуга"""
    additional_service = models.ForeignKey(AdditionalService, on_delete=models.CASCADE, )

    """Additional service price / Стоимость дополнительной услуги"""
    price = models.DecimalField(max_digits=16, decimal_places=9)

    def __str__(self):
        return self.name
