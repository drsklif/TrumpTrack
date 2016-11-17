# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov
Transportation request model description / Описание модели заявки на транспортировку
"""

from django.db import models

from api.models.contractor import Contractor
from api.models.parcel_size import ParcelSize

__author__ = 'ildyakov'


class TransportationRequest(models.Model):
    """
    Transportation request / Заявка на транспортировку
    """

    """Client / Заказчик"""
    client = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='transportation_requests',)

    """Loading address / Адрес погрузки"""
    address_from = models.CharField(max_length=250)

    """Unloading address / Адрес разгрузки"""
    address_to = models.CharField(max_length=250)

    """Departure date / Дата отправки"""
    date_departure = models.DateField()

    """Description / Описание"""
    description = models.CharField(max_length=1024, blank=True)

    """Parcel weight / Вес отправления"""
    weight = models.FloatField()

    """Parcel size / Размер отправления"""
    size = models.ForeignKey(ParcelSize, on_delete=models.CASCADE, related_name='+',)

    def __str__(self):
        return "{}, {}. From {} To {}".format(self.client.name, self.date_departure, self.address_from, self.address_to)
