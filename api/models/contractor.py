# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov
Contractor model description / Описание модели Контрагента
"""

from django.db import models

from api.models.property_type import PropertyType
from api.models.contractor_status import ContractorStatus


class Contractor(models.Model):
    """
    Contractor / Контрагент
    """

    """Contractor name / Название организации"""
    name = models.CharField(max_length=256, blank=False)

    """Contractor full name / Полное название организации"""
    full_name = models.CharField(max_length=1024, blank=False, null=True)

    """Contractor property type / Тип собственности организации"""
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name='+',)

    """Contractor status / Статус организации"""
    status = models.ForeignKey(ContractorStatus, on_delete=models.CASCADE, related_name='+',)

    """Phone numbers / Номера телефонов"""
    phone = models.CharField(max_length=150, blank=True)

    """Fax numbers / Номера факсов"""
    fax = models.CharField(max_length=150, blank=True)

    """Email"""
    email = models.EmailField(max_length=150, blank=True)

    """Legal address / Юридический адрес"""
    address_legal = models.CharField(max_length=250, blank=True)

    """Actual address / Фактический адрес"""
    address_actual = models.CharField(max_length=250, blank=True)

    """Mailing address / Почтовый адрес"""
    address_mailing = models.CharField(max_length=250, blank=True)

    """Notes / Заметки"""
    notes = models.CharField(max_length=2048, blank=True)

    def __str__(self):
        return self.name
