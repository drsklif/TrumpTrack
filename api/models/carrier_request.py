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

    sender = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )
    """Sender / Отправитель"""

    loading_address = models.CharField(max_length=256)
    """Loading address / Адрес погрузки"""

    loading_contacts = models.CharField(max_length=256, blank=True)
    """Loading contacts / Контакты на месте погрузки"""

    recipient = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )
    """Recipient / Получатель"""

    landing_address = models.CharField(max_length=256)
    """Landing address / Адрес выгрузки"""

    landing_contacts = models.CharField(max_length=256, blank=True)
    """Landing contacts / Контакты на месте выгрузки"""

    vehicle = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )
    """Vehicle / Транспортное средство"""

    driver = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )
    """Driver / Водитель"""

    carrier = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )
    """Carrier / Перевозчик"""

    department = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )
    """Department / Подразделение"""

    payment_type = models.ForeignKey(Contractor, on_delete=models.CASCADE, related_name='+', )
    """Payment type / Вид расчета"""

    cost = models.DecimalField(max_digits=16, decimal_places=9)
    """Cost / Стоимость"""

    invoice_number = models.CharField(max_length=20)
    """Invoice number / Номер выставленного счета"""

    invoice_date = models.DateField()
    """Invoice date / Дата выставленного счета"""

    payment_date = models.DateField()
    """Payment date / Дата оплаты"""

    delay = models.BooleanField()
    """Possibility of postponing / Возможность отсрочки"""
