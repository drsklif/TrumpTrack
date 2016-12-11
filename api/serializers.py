# -*- coding: utf-8 -*-

"""
Created on 11.12.2016

:author: Alexander Ildyakov

Models serializers / Сериализаторы моделей
"""

from api.models.property_type import PropertyType
from api.models.contractor_status import ContractorStatus
from api.models.contractor import Contractor
from api.models.parcel_size import ParcelSize
from api.models.tr_type import TransportationRequestType
from api.models.tr_status import TransportationRequestStatus
from api.models.tr import TransportationRequest
from rest_framework import serializers

__author__ = 'ildyakov'


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ('id', 'name',)


class ContractorStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorStatus
        fields = ('id', 'name', )


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ('id', 'name', 'full_name', 'property_type', 'status', 'phone', 'fax', 'email', 'address_legal',
                  'address_actual', 'address_mailing', 'notes',)


class ParcelSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelSize
        fields = ('id', 'size', )


class TransportationRequestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationRequestType
        fields = ('id', 'name',)


class TransportationRequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationRequestStatus
        fields = ('id', 'name', )


class TransportationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationRequest
        fields = ('id', 'client', 'address_from', 'address_to', 'date_departure', 'description', 'weight', 'size',
                  'type', 'status',)
