# -*- coding: utf-8 -*-

"""
Created on 06.12.2016

:author: Alexander Ildyakov
api tests
"""

from django.test import TestCase

# Create your tests here.
from api.models import Contractor, ContractorStatus, PropertyType
#, TransportationRequest, TransportationRequestType, TransportationRequestStatus

__author__ = 'ildyakov'


class TestContractor(TestCase):
    fixtures = [
        'api/fixtures/initial_system.json',
        'api/fixtures/initial_user.json',
    ]

    @classmethod
    def setUp(cls):
        cls.contractor_status = ContractorStatus.objects.get(pk=1)
        cls.property_type = PropertyType.objects.get(pk=1)

    def test_contractor_creation(self):
        contractor = Contractor.objects.create(
            name="test client",
            property_type=self.property_type,
            status=self.contractor_status,
            phone="123456789",
            email="some@email.ru",
            address_legal="some address",
        )
        print(contractor.status.name)
        print(contractor.property_type.name)
        assert contractor.pk is not None

class TestTransportationRequest(TestCase):
    @classmethod
    def setUp(cls):
         pass

    def test_TR_creation(self):
        assert 1!=2
