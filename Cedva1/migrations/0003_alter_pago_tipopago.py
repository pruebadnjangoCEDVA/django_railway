# Generated by Django 4.1.1 on 2022-12-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cedva1', '0002_alter_alumno_activo_por_pagos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='tipoPago',
            field=models.CharField(choices=[('p', 'Seleccione opción'), ('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'), ('Depósito', 'Depósito'), ('Mercado Libre', 'Mercado Libre')], default='p', max_length=100),
        ),
    ]
