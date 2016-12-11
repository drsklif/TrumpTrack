# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov

Forward voucher expenses / Дополнительные затраты экспедиторской расписки

User data type / Пользовательский тип данных
"""

from django.db import models
from api.models.add_service import AdditionalService
from api.models.forward_voucher import ForwardVoucher

__author__ = 'ildyakov'


class ForwardVoucherExpenses(models.Model):
    """
    Forward expenses / Дополнительные затраты
    """

    forward_voucher = models.ForeignKey(ForwardVoucher, on_delete=models.CASCADE,)
    """Forward voucher / Экспедиторская расписка"""

    additional_service = models.ForeignKey(AdditionalService, on_delete=models.CASCADE, )
    """Additional service / Дополнительная услуга"""

    price = models.DecimalField(max_digits=16, decimal_places=9)
    """Additional service price / Стоимость дополнительной услуги"""

    def __str__(self):
        return self.name
