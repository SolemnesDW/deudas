# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deudas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acreedor', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('fehca_inicio', models.DateTimeField()),
                ('monto', models.IntegerField(default=0)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deudor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('apellido_paterno', models.CharField(max_length=200)),
                ('apellido_materno', models.CharField(max_length=200)),
                ('estado_Civil', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='deudas',
            name='Deudor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deudas.Deudor'),
        ),
    ]
