# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('full_name', models.CharField(max_length=1024, null=True)),
                ('phone', models.CharField(blank=True, max_length=150)),
                ('fax', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('address_legal', models.CharField(blank=True, max_length=250)),
                ('address_actual', models.CharField(blank=True, max_length=250)),
                ('address_mailing', models.CharField(blank=True, max_length=250)),
                ('notes', models.CharField(blank=True, max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='ContractorStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=256)),
                ('first_name', models.CharField(blank=True, max_length=256)),
                ('part_name', models.CharField(blank=True, max_length=256)),
                ('passport_series', models.CharField(max_length=5)),
                ('passport_number', models.CharField(max_length=6)),
                ('passport_issue_date', models.DateField()),
                ('passport_subdivision_code', models.CharField(max_length=7)),
                ('passport_issuer', models.CharField(max_length=256)),
                ('passport_place_of_birth', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PackagingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ParcelSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XL', 'Large'), ('MD', 'Medium'), ('SM', 'Small')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=256)),
                ('first_name', models.CharField(blank=True, max_length=256)),
                ('part_name', models.CharField(blank=True, max_length=256)),
                ('phone', models.CharField(blank=True, max_length=150)),
                ('fax', models.CharField(blank=True, max_length=150)),
                ('email', models.CharField(blank=True, max_length=150)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='api.Contractor')),
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
            name='TransportationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_from', models.CharField(max_length=250)),
                ('address_to', models.CharField(max_length=250)),
                ('date_departure', models.DateField()),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('weight', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportation_requests', to='api.Contractor')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.ParcelSize')),
            ],
        ),
        migrations.CreateModel(
            name='TransportationRequestStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TransportationRequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('tractor_number', models.CharField(max_length=50)),
                ('trailer_number', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=256)),
                ('owner_address', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.VehicleType'),
        ),
        migrations.AddField(
            model_name='transportationrequest',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.TransportationRequestStatus'),
        ),
        migrations.AddField(
            model_name='transportationrequest',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.TransportationRequestType'),
        ),
        migrations.AddField(
            model_name='person',
            name='transportation_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='api.TransportationRequest'),
        ),
        migrations.AddField(
            model_name='contractor',
            name='property_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.PropertyType'),
        ),
        migrations.AddField(
            model_name='contractor',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.ContractorStatus'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='packaging_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.PackagingType'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.ParcelSize'),
        ),
    ]