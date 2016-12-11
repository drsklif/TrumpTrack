# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov

Property type model description / Описание модели типа собственности

User data type / Пользовательский тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class PropertyType(models.Model):
    """
    Property type / Тип собственности
    """

    name = models.CharField(max_length=50)
    """Property type name / Название типа собственности"""

    def __str__(self):
        return self.name
