from django.db import models
from django.db.models import Manager

__author__ = 'ildyakov'


class PropertyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ParcelSize(models.Model):
    LARGE = ('XL', 'Large')
    MEDIUM = ('MD', 'Medium')
    SMALL = ('SM', 'Small')
    __all = (LARGE, MEDIUM, SMALL)

    size = models.CharField(max_length=2, choices=__all)

    def __str__(self):
        return self.size


class Request(models.Model):
    company = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    property_type = models.ForeignKey(PropertyType, related_name='requests')
    address_from = models.CharField(max_length=250)
    address_to = models.CharField(max_length=250)
    date_send = models.DateField()
    description = models.CharField(max_length=1024)
    weight = models.FloatField()
    size = models.ForeignKey('ParcelSize', related_name='requests')

    objects = Manager()

    def __str__(self):
        return "{}, {}. From {} To {}".format(self.company, self.date_send, self.address_from, self.address_to)
