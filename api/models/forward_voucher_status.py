# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov
Forward voucher status model description / Описание модели статуса экспедиторской расписки
"""

from django.db import models

__author__ = 'ildyakov'


class ForwardVoucherStatus(models.Model):
    """
    Forward voucher status / Статус экспедиторской расписки
    """

    """Status name / Название статуса"""
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
