# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov
Person model description / Описание модели персоны
"""

from django.db import models

from api.models.contractor import Contractor
from api.models.tr import TransportationRequest

__author__ = 'ildyakov'


class Person(models.Model):
    """
    Person / Персона
    """

    """Last name / Фамилия"""
    last_name = models.CharField(max_length=256, blank=True)

    """First name / Имя"""
    first_name = models.CharField(max_length=256, blank=True)

    """Part name / Отчество"""
    part_name = models.CharField(max_length=256, blank=True)

    """Phone numbers / Номера телефонов"""
    phone = models.CharField(max_length=150, blank=True)

    """Fax numbers / Номера факсов"""
    fax = models.CharField(max_length=150, blank=True)

    """Email"""
    email = models.CharField(max_length=150, blank=True)

    """Contractor / Контрагент"""
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='persons',)

    """Transportation requests / Заявки на транспортировку"""
    transportation_request = models.ForeignKey(TransportationRequest, on_delete=models.CASCADE, related_name='persons',)

    def __str__(self):
        return self.name
