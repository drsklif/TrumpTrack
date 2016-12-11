# -*- coding: utf-8 -*-

"""
Created on 20.11.2016

:author: Alexander Ildyakov

Vehicle model description / Описание модели транспортного средства

User data type / Пользовательский тип данных
"""

from django.db import models
from api.models.vehicle_type import VehicleType

__author__ = 'ildyakov'


class Vehicle(models.Model):
    """
    Vehicle reference / Справочник транспортных средств
    """

    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, related_name='+',)
    """Vehicle type / Тип ТС"""

    model = models.CharField(max_length=50)
    """Vehicle model / Марка ТС"""

    tractor_number = models.CharField(max_length=50)
    """Tractor number / Гос. номер тягача"""

    trailer_number = models.CharField(max_length=50)
    """Trailer number / Гос. номер прицепа"""

    owner = models.CharField(max_length=256)
    """Vehicle owner / Владелец ТС"""

    owner_address = models.CharField(max_length=256)
    """Vehicle owner address / Адрес владельца ТС"""

    def __str__(self):
        return self.name
