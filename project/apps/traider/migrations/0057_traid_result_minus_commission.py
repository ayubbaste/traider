# Generated by Django 3.2.12 on 2022-02-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0056_screenshot_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='traid',
            name='result_minus_commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50, verbose_name='Результат - коммиссия'),
        ),
    ]
