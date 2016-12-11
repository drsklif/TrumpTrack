# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov

Contractor status model description / Описание модели статуса контрагента

System data type / Системный тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class ContractorStatus(models.Model):
    """
    Contractor status / Статус контрагента
    """

    name = models.CharField(max_length=256)
    """Status name / Название статуса"""

    def __str__(self):
        return self.name
