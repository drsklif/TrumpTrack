# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov
Shipment status reference / Справочник статусов отправки
"""

from django.db import models

__author__ = 'ildyakov'


class ShipmentStatus(models.Model):
    """
    Shipment status reference / Справочник статусов отправки
    """

    """Status name / Название статуса"""
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
