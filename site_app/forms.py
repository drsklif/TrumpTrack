# -*- coding: utf-8 -*-

from django import forms

from api.models.property_type import PropertyType
from api.models.tr import TransportationRequest

__author__ = 'ildyakov'


class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = [
            'name',
        ]


class RequestForm(forms.ModelForm):
    class Meta:
        model = TransportationRequest
        fields = '__all__'
