# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov

Contractor model description / Описание модели Контрагента

User data type / Пользовательский тип данных
"""

from django.db import models

from api.models.property_type import PropertyType
from api.models.contractor_status import ContractorStatus


class Contractor(models.Model):
    """
    Contractor / Контрагент
    """

    name = models.CharField(max_length=256, blank=False)
    """Contractor name / Название организации"""

    full_name = models.CharField(max_length=1024, blank=False, null=True)
    """Contractor full name / Полное название организации"""

    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name='+',)
    """Contractor property type / Тип собственности организации"""

    status = models.ForeignKey(ContractorStatus, on_delete=models.CASCADE, related_name='+',)
    """Contractor status / Статус организации"""

    phone = models.CharField(max_length=150, blank=True)
    """Phone numbers / Номера телефонов"""

    fax = models.CharField(max_length=150, blank=True)
    """Fax numbers / Номера факсов"""

    email = models.EmailField(max_length=150, blank=True)
    """Email"""

    address_legal = models.CharField(max_length=250, blank=True)
    """Legal address / Юридический адрес"""

    address_actual = models.CharField(max_length=250, blank=True)
    """Actual address / Фактический адрес"""

    address_mailing = models.CharField(max_length=250, blank=True)
    """Mailing address / Почтовый адрес"""

    notes = models.CharField(max_length=2048, blank=True)
    """Notes / Заметки"""

    def __str__(self):
        return self.name
