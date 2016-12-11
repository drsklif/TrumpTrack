# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov

Person model description / Описание модели персоны

User data type / Пользовательский тип данных
"""

from django.db import models

from api.models.contractor import Contractor
from api.models.tr import TransportationRequest

__author__ = 'ildyakov'


class Person(models.Model):
    """
    Person / Персона
    """

    last_name = models.CharField(max_length=256, blank=True)
    """Last name / Фамилия"""

    first_name = models.CharField(max_length=256, blank=True)
    """First name / Имя"""

    part_name = models.CharField(max_length=256, blank=True)
    """Part name / Отчество"""

    phone = models.CharField(max_length=150, blank=True)
    """Phone numbers / Номера телефонов"""

    fax = models.CharField(max_length=150, blank=True)
    """Fax numbers / Номера факсов"""

    email = models.CharField(max_length=150, blank=True)
    """Email"""

    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='persons',)
    """Contractor / Контрагент"""

    transportation_request = models.ForeignKey(TransportationRequest, on_delete=models.CASCADE, related_name='persons',)
    """Transportation requests / Заявки на транспортировку"""

    def __str__(self):
        return self.name
