# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov

Forward voucher status model description / Описание модели статуса экспедиторской расписки

System data type / Системный тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class ForwardVoucherStatus(models.Model):
    """
    Forward voucher status / Статус экспедиторской расписки
    """

    name = models.CharField(max_length=256)
    """Status name / Название статуса"""

    def __str__(self):
        return self.name
