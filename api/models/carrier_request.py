# -*- coding: utf-8 -*-

"""
Created on 21.11.2016

:author: Alexander Ildyakov

Carrier request / Заявка с перевозчиком

User data type / Пользовательский тип данных
"""

from django.db import models

from api.models.contractor import Contractor

__author__ = 'ildyakov'


class CarrierRequest(models.Model):
    """
    Carrier request / Заявка с перевозчиком
    """

    """Sender / Отправитель"""
    sender = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Loading address / Адрес погрузки"""
    loading_address = models.CharField(max_length=256)

    """Loading contacts / Контакты на месте погрузки"""
    loading_contacts = models.CharField(max_length=256, blank=True)

    """Recipient / Получатель"""
    recipient = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Landing address / Адрес выгрузки"""
    landing_address = models.CharField(max_length=256)

    """Landing contacts / Контакты на месте выгрузки"""
    landing_contacts = models.CharField(max_length=256, blank=True)

    """Vehicle / Транспортное средство"""
    vehicle = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Driver / Водитель"""
    driver = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Carrier / Перевозчик"""
    carrier = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Department / Подразделение"""
    department = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Payment type / Вид расчета"""
    payment_type = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )

    """Cost / Стоимость"""
    cost = models.DecimalField(max_digits=16, decimal_places=9)

    """Invoice number / Номер выставленного счета"""
    invoice_number = models.CharField(max_length=20)

    """Invoice date / Дата выставленного счета"""
    invoice_date = models.DateField()

    """Payment date / Дата оплаты"""
    payment_date = models.DateField()

    """Possibility of postponing / Возможность отсрочки"""
    delay = models.BooleanField()
