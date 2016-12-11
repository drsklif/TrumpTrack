# -*- coding: utf-8 -*-

"""
Created on 20.11.2016

:author: Alexander Ildyakov

Cargo reference / Справочник грузов

User data type / Пользовательский тип данных
"""

from django.db import models
from api.models.packaging_type import PackagingType
from api.models.parcel_size import ParcelSize

__author__ = 'ildyakov'


class Cargo(models.Model):
    """
    Cargo reference / Справочник грузов
    """

    name = models.CharField(max_length=50)
    """Cargo name / Наименование груза"""

    packaging_type = models.ForeignKey(PackagingType, on_delete=models.CASCADE, related_name='+',)
    """Cargo packaging type / Тип упаковки груза"""

    weight = models.FloatField()
    """Weight / Вес"""

    size = models.ForeignKey(ParcelSize, on_delete=models.CASCADE, related_name='+', )
    """Size / Размер"""

    def __str__(self):
        return self.name
