# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov

Payment type reference / Справочник видов расчета

System data type / Системный тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class PaymentType(models.Model):
    """
    Payment type reference / Справочник видов расчета
    """

    name = models.CharField(max_length=50)
    """Payment type name / Наименование вида расчета"""

    def __str__(self):
        return self.name
