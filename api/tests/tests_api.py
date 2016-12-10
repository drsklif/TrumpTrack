# -*- coding: utf-8 -*-

"""
Created on 06.12.2016

:author: Alexander Ildyakov
api tests
"""

from django.test import TestCase
from datetime import datetime

# Create your tests here.
from api.models import Contractor, ContractorStatus, PropertyType,\
    ParcelSize, TransportationRequest, TransportationRequestType, TransportationRequestStatus

__author__ = 'ildyakov'


class TestContractor(TestCase):
    property_type = None
    contractor_status = None

    fixtures = [
        'api/fixtures/initial_system.json',
        'api/fixtures/initial_user.json',
    ]

    @classmethod
    def setUp(cls):
        print()
        cls.contractor_status = ContractorStatus.objects.get(pk=1)
        print("successfully fetched contractor status \"{}\"".format(cls.contractor_status.name))
        cls.property_type = PropertyType.objects.get(pk=1)
        print("successfully fetched property type \"{}\"".format(cls.property_type.name))

    @classmethod
    def create_contractor(cls):
        contractor = Contractor.objects.create(
            name="test client",
            property_type=cls.property_type,
            status=cls.contractor_status,
            phone="123456789",
            email="some@email.ru",
            address_legal="some address",
        )
        return contractor

    def test_contractor_creation(self):
        contractor = self.create_contractor()
        assert contractor.pk is not None
        print("contractor successfully created, id: {}".format(contractor.pk))
        print("contractor status \"{}\"".format(contractor.status.name))
        print("contractor property type \"{}\"".format(contractor.property_type.name))
        print("test_contractor_creation passed!")


class TestTransportationRequest(TestCase):
    client = None
    size = None
    type = None
    status = None

    fixtures = [
        'api/fixtures/initial_system.json',
        'api/fixtures/initial_user.json',
    ]

    @classmethod
    def setUp(cls):
        print()
        cls.size = ParcelSize.objects.get(pk=1)
        print("successfully fetched parcel size \"{}\"".format(cls.size.size))
        cls.type = TransportationRequestType.objects.get(pk=1)
        print("successfully fetched transportation request type \"{}\"".format(cls.type.name))
        cls.status = TransportationRequestStatus.objects.get(pk=1)
        print("successfully fetched transportation request status \"{}\"".format(cls.status.name))
        cls.client = TestContractor.create_contractor()
        print("contractor successfully created, id: {}".format(cls.client.pk))

    @classmethod
    def create_transportation_request(cls):
        tr = TransportationRequest.objects.create(
            client=cls.client,
            address_from="addr 1",
            address_to="addr 2",
            date_departure=datetime.now(),
            description="first request",
            weight=1.1,
            size=cls.size,
            type=cls.type,
            status=cls.status
        )
        return tr

    def test_tr_creation(self):
        tr = self.create_transportation_request()
        assert tr.pk is not None
        print("transportation request successfully created, id: {}".format(tr.pk))
        print("transportation request client \"{}\"".format(tr.client.name))
        print("transportation request type \"{}\"".format(tr.type.name))
        print("transportation request size \"{}\"".format(tr.size.size))
        print("transportation request status \"{}\"".format(tr.status.name))
        print("test_tr_creation passed!")
