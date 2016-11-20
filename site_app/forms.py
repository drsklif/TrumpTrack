# -*- coding: utf-8 -*-

from django import forms

from site_app.models import Request, PropertyType

__author__ = 'ildyakov'


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
