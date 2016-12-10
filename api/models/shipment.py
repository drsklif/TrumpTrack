# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov

Shipment / Отправка

User data type / Пользовательский тип данных
"""

from django.db import models

from api.models.carrier_request import CarrierRequest
from api.models.shipment_status import ShipmentStatus

__author__ = 'ildyakov'


class Shipment(models.Model):
    """
    Shipment / Отправка
    """

    """Shipment status / Статус отправки"""
    status = models.ForeignKey(ShipmentStatus, on_delete=models.CASCADE, related_name='+',)

    """Sending date / Дата отправки"""
    date_sending = models.DateField()

    """Arrival date planed / Дата прибытия планируемая"""
    date_arrival_plan = models.DateField()

    """Arrival date fact / Дата прибытия фактическая"""
    date_arrival_fact = models.DateField()

    """Carrier request / Заявка с перевозчиком"""
    carrier_request = models.ForeignKey(CarrierRequest, on_delete=models.CASCADE, related_name='shipments', )

    def __str__(self):
        return self.name
