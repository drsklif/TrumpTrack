# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov
Cargo state reference / Справочник состояний грузов
User data type / Пользовательский тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class CargoState(models.Model):
    """
    Cargo state reference / Справочник состояний грузов
    """

    """Cargo state name / Наименование состояния груза"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
