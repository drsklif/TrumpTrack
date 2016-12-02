# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov
Forward voucher / Экспедиторская расписка
User data type / Пользовательский тип данных
"""

from django.db import models

from api.models.add_service import AdditionalService
from api.models.parcel_size import ParcelSize
from api.models.contractor import Contractor
from api.models.forward_voucher_type import ForwardVoucherType
from api.models.forward_voucher_status import ForwardVoucherStatus
from api.models.cargo import Cargo
from api.models.cargo_state import CargoState
from api.models.packaging_type import PackagingType
from api.models.shipment import Shipment

__author__ = 'ildyakov'


class ForwardVoucher(models.Model):
    """
    Forward voucher / Экспедиторская расписка
    """

    """Forward voucher type / Тип экспедиторской расписки"""
    fv_type = models.ForeignKey(ForwardVoucherType, on_delete=models.CASCADE, related_name='+', default=1)

    """Forward voucher status / Статус экспедиторской расписки"""
    status = models.ForeignKey(ForwardVoucherStatus, on_delete=models.CASCADE, related_name='+', )

    """Department / Подразделение (своя организация. для выставления счетов)"""
    department = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+',)

    """Customer / Заказчик"""
    customer = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Sender / Отправитель"""
    sender = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Recipient / Получатель"""
    recipient = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Cargo / Наименование груза"""
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='+', )

    """Cargo packaging type / Тип упаковки груза"""
    packaging_type = models.ForeignKey(PackagingType, on_delete=models.CASCADE, related_name='+', )

    """Cargo state / Состояние груза"""
    cargo_state = models.ForeignKey(CargoState, on_delete=models.CASCADE, related_name='+', )

    """Cargo price / Оценочная стоимость груза"""
    cargo_price = models.DecimalField(max_digits=16, decimal_places=9)

    """Places count / Количество мест"""
    places_count = models.IntegerField()

    """Parcel weight / Вес отправления"""
    weight = models.FloatField()

    """Parcel size / Размер отправления"""
    size = models.ForeignKey(ParcelSize, on_delete=models.CASCADE, related_name='+', )

    """Destination station / Станция назначения"""
    destination_station = models.CharField(max_length=256)

    """Documents number / № сопроводительных документов"""
    documents_number = models.CharField(max_length=50)

    """Shipment price / Сумма перевозки"""
    shipment_price = models.DecimalField(max_digits=16, decimal_places=9)

    """Description / Описание"""
    description = models.CharField(max_length=1024, blank=True)

    expenses = models.ManyToManyField(AdditionalService, through='ForwardVoucherExpenses')

    """Shipment / Отправка"""
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='forward_vouchers', )

    def __str__(self):
        return "{}, {}. From {} To {}".format(self.client.name, self.date_departure, self.address_from, self.address_to)
