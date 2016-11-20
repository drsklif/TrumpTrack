# -*- coding: utf-8 -*-

"""
Created on 20.11.2016

:author: Alexander Ildyakov
Packaging type model description / Описание модели типа упаковки
"""

from django.db import models

__author__ = 'ildyakov'


class PackagingType(models.Model):
    """
    Packaging type reference / Справочник видов упаковок
    """

    """Packaging type name / Наименование вида упаковки"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
