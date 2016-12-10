# -*- coding: utf-8 -*-

"""
Created on 18.11.2016

:author: Alexander Ildyakov

Transportation request status model description / Описание модели статуса заявки на транспортировку

User data type / Пользовательский тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class TransportationRequestStatus(models.Model):
    """
    Transportation request status / Статус заявки на транспортировку
    """

    """Status name / Название статуса"""
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
