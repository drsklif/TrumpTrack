# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov

Transportation request model description / Описание модели заявки на транспортировку

User data type / Пользовательский тип данных
"""

from django.db import models

from api.models.contractor import Contractor
from api.models.parcel_size import ParcelSize
from api.models.tr_type import TransportationRequestType
from api.models.tr_status import TransportationRequestStatus

__author__ = 'ildyakov'


class TransportationRequest(models.Model):
    """
    Transportation request / Заявка на транспортировку
    """

    client = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='transportation_requests',)
    """Client / Заказчик"""

    address_from = models.CharField(max_length=250)
    """Loading address / Адрес погрузки"""

    address_to = models.CharField(max_length=250)
    """Unloading address / Адрес разгрузки"""

    date_departure = models.DateField()
    """Departure date / Дата отправки"""

    description = models.CharField(max_length=1024, blank=True)
    """Description / Описание"""

    weight = models.FloatField()
    """Parcel weight / Вес отправления"""

    size = models.ForeignKey(ParcelSize, on_delete=models.CASCADE, related_name='+',)
    """Parcel size / Размер отправления"""

    type = models.ForeignKey(TransportationRequestType, on_delete=models.CASCADE, related_name='+', )
    """Request type / Тип заявки"""

    status = models.ForeignKey(TransportationRequestStatus, on_delete=models.CASCADE, related_name='+', )
    """Request status / Статус заявки"""

    def __str__(self):
        return "{}, {}. From {} To {}".format(self.client.name, self.date_departure, self.address_from, self.address_to)
