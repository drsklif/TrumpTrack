# -*- coding: utf-8 -*-

"""
Created on 11.12.2016

:author: Alexander Ildyakov

Models serializers / Сериализаторы моделей
"""

import django_filters
from api.models.contractor import Contractor

__author__ = 'ildyakov'


class ContractorFilter(django_filters.FilterSet):
    """
    Contractor filter by name
    """

    name = django_filters.CharFilter(name="name", lookup_expr="contains")
    """name field filter options"""

    class Meta:
        model = Contractor
        fields = ['name']
