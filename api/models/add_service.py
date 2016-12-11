# -*- coding: utf-8 -*-

"""
Created on 20.11.2016

:author: Alexander Ildyakov

Additional services model description / Описание модели дополнительных услуг

User data type / Пользовательский тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class AdditionalService(models.Model):
    """
    Additional services reference / Справочник дополнительных услуг
    """

    name = models.CharField(max_length=50)
    """Additional service name / Название дополнительной услуги"""

    price = models.DecimalField(max_digits=16, decimal_places=9)
    """Additional service price / Стоимость дополнительной услуги"""

    def __str__(self):
        return self.name
