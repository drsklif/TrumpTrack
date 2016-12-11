# -*- coding: utf-8 -*-

"""
Created on 28.11.2016

:author: Alexander Ildyakov

Forward voucher type type / Справочник типов экспедиционных расписок

System data type / Системный тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class ForwardVoucherType(models.Model):
    """
    Packaging type reference / Справочник видов упаковок
    """

    name = models.CharField(max_length=50)
    """Packaging type name / Наименование вида упаковки"""

    def __str__(self):
        return self.name
