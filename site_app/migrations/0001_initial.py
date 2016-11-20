# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParcelSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XL', 'Large'), ('MD', 'Medium'), ('SM', 'Small')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
                ('address_from', models.CharField(max_length=250)),
                ('address_to', models.CharField(max_length=250)),
                ('date_send', models.DateField()),
                ('description', models.CharField(max_length=1024)),
                ('weight', models.FloatField()),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='site_app.PropertyType')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='site_app.ParcelSize')),
            ],
        ),
    ]
