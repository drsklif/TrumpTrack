# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov
Property type model description / Описание модели типа собственности
"""

from django.db import models

__author__ = 'ildyakov'


class PropertyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
