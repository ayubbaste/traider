# Generated by Django 3.2.8 on 2021-10-12 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0010_alter_traid_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traid',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Время выхода'),
        ),
        migrations.AlterField(
            model_name='traid',
            name='sell_perc_avg',
            field=models.DecimalField(decimal_places=4, default=0, editable=False, max_digits=8, verbose_name='Средний процент продажи'),
        ),
        migrations.AlterField(
            model_name='traid',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Время входа'),
        ),
    ]
