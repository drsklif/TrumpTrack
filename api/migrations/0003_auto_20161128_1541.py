# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161121_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForwardVoucherType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='forwardvoucher',
            name='fv_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.ForwardVoucherType'),
        ),
    ]
