# -*- coding: utf-8 -*-

"""
Created on 20.11.2016

:author: Alexander Ildyakov

Driver model description / Описание модели водителя

User data type / Пользовательский тип данных
"""

from django.db import models

__author__ = 'ildyakov'


class Driver(models.Model):
    """
    Driver reference / Справочник водителей
    """

    """Last name / Фамилия"""
    last_name = models.CharField(max_length=256, blank=True)

    """First name / Имя"""
    first_name = models.CharField(max_length=256, blank=True)

    """Part name / Отчество"""
    part_name = models.CharField(max_length=256, blank=True)

    """Passport series / Серия паспорта"""
    passport_series = models.CharField(max_length=5)

    """Passport number / Номер паспорта"""
    passport_number = models.CharField(max_length=6)

    """Passport issue date / Дата выдачи паспорта"""
    passport_issue_date = models.DateField()

    """Passport subdivision code / Паспорт, код подразделения"""
    passport_subdivision_code = models.CharField(max_length=7)

    """Passport issuer / Орган выдачи паспорта"""
    passport_issuer = models.CharField(max_length=256)

    """Passport passport place of birth / Место рождения"""
    passport_place_of_birth = models.CharField(max_length=256)

    def __str__(self):
        return self.name
