# -*- coding: utf-8 -*-

"""
Created on 17.11.2016

:author: Alexander Ildyakov
Parcel size model description / Описание модели размера отправления
"""

from django.db import models

__author__ = 'ildyakov'


class ParcelSize(models.Model):
    LARGE = ('XL', 'Large')
    MEDIUM = ('MD', 'Medium')
    SMALL = ('SM', 'Small')
    __all = (LARGE, MEDIUM, SMALL)

    size = models.CharField(max_length=2, choices=__all)

    def __str__(self):
        return self.size
