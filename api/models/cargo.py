# -*- coding: utf-8 -*-

"""
Created on 20.11.2016

:author: Alexander Ildyakov
Cargo reference / Справочник грузов
"""

from django.db import models
from api.models.packaging_type import PackagingType
from api.models.parcel_size import ParcelSize

__author__ = 'ildyakov'


class Cargo(models.Model):
    """
    Cargo reference / Справочник грузов
    """

    """Cargo name / Наименование груза"""
    name = models.CharField(max_length=50)

    """Cargo packaging type / Тип упаковки груза"""
    packaging_type = models.ForeignKey(PackagingType, on_delete=models.CASCADE, related_name='+',)

    """Weight / Вес"""
    weight = models.FloatField()

    """Size / Размер"""
    size = models.ForeignKey(ParcelSize, on_delete=models.CASCADE, related_name='+', )

    def __str__(self):
        return self.name
