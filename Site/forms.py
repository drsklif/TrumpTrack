# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

from Site.models import Request, PropertyType

__author__ = 'sobolevn'


class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = [
            'name',
        ]


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
