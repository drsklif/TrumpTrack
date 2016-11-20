# -*- coding: utf-8 -*-

"""
Created on 18.11.2016

:author: Alexander Ildyakov
Transportation request type model description / Описание модели типа заявки на транспортировку
"""

from django.db import models

__author__ = 'ildyakov'


class TransportationRequestType(models.Model):
    """
    Transportation request type reference / Справочник типов заявок на транспортировку
    """

    """Request type name / Название типа заявки"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
