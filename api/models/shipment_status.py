# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov

Shipment status reference / Справочник статусов отправки

System data type / Системный тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class ShipmentStatus(models.Model):
    """
    Shipment status reference / Справочник статусов отправки
    """

    name = models.CharField(max_length=256)
    """Status name / Название статуса"""

    def __str__(self):
        return self.name
