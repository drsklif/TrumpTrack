# -*- coding: utf-8 -*-

"""
Created on 20.11.2016

:author: Alexander Ildyakov
Additional services model description / Описание модели дополнительных услуг
"""

from django.db import models

__author__ = 'ildyakov'


class AdditionalService(models.Model):
    """
    Additional services reference / Справочник дополнительных услуг
    """

    """Additional service name / Название дополнительной услуги"""
    name = models.CharField(max_length=50)

    """Additional service price / Стоимость дополнительной услуги"""
    price = models.DecimalField()

    def __str__(self):
        return self.name