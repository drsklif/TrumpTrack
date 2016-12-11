# -*- coding: utf-8 -*-

"""
Created on 11.12.2016

:author: Alexander Ildyakov

Models serializers / Сериализаторы моделей
"""

from rest_framework import viewsets
from api.models.property_type import PropertyType
from api.models.contractor_status import ContractorStatus
from api.models.contractor import Contractor
from api.models.parcel_size import ParcelSize
from api.models.tr_type import TransportationRequestType
from api.models.tr_status import TransportationRequestStatus
from api.models.tr import TransportationRequest
from api.serializers import PropertyTypeSerializer, ContractorStatusSerializer, ContractorSerializer
from api.serializers import ParcelSizeSerializer, TransportationRequestTypeSerializer, \
    TransportationRequestStatusSerializer, TransportationRequestSerializer
from api import filters

__author__ = 'ildyakov'


class PropertyTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows property types to be viewed or edited.
    """
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer


class ContractorStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contractor statuses to be viewed or edited.
    """
    queryset = ContractorStatus.objects.all()
    serializer_class = ContractorStatusSerializer
    http_method_names = ['get', 'options']


class ContractorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contractors to be viewed or edited.
    """
    queryset = Contractor.objects.all().order_by('-id')
    serializer_class = ContractorSerializer
    filter_fields = ('name',)
    filter_class = filters.ContractorFilter


class ParcelSizeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parcel sizes to be viewed or edited.
    """
    queryset = ParcelSize.objects.all()
    serializer_class = ParcelSizeSerializer
    http_method_names = ['get', 'options']


class TransportationRequestTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transportation request types to be viewed or edited.
    """
    queryset = TransportationRequestType.objects.all()
    serializer_class = TransportationRequestTypeSerializer
    http_method_names = ['get', 'options']


class TransportationRequestStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transportation request statuses to be viewed or edited.
    """
    queryset = TransportationRequestStatus.objects.all()
    serializer_class = TransportationRequestStatusSerializer
    http_method_names = ['get', 'options']


class TransportationRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transportation requests to be viewed or edited.
    """
    queryset = TransportationRequest.objects.all().order_by('-id')
    serializer_class = TransportationRequestSerializer
