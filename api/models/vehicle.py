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

    """Vehicle type / Тип ТС"""
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, related_name='+',)

    """Vehicle model / Марка ТС"""
    model = models.CharField(max_length=50)

    """Tractor number / Гос. номер тягача"""
    tractor_number = models.CharField(max_length=50)

    """Trailer number / Гос. номер прицепа"""
    trailer_number = models.CharField(max_length=50)

    """Vehicle owner / Владелец ТС"""
    owner = models.CharField(max_length=256)

    """Vehicle owner address / Адрес владельца ТС"""
    owner_address = models.CharField(max_length=256)

    def __str__(self):
        return self.name
