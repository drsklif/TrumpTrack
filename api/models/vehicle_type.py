# -*- coding: utf-8 -*-

"""
Created on 20.11.2016

:author: Alexander Ildyakov

Vehicle type model description / Описание модели типа транспортного средства

User data type / Пользовательский тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class VehicleType(models.Model):
    """
    Vehicle type reference / Справочник типов транспортных средств
    """

    name = models.CharField(max_length=50)
    """Vehicle type name / Наименование транспортного средства"""

    def __str__(self):
        return self.name
