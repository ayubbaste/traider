# Generated by Django 4.0.1 on 2022-01-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0047_traid_result_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='traid',
            name='stoploss_percent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, verbose_name='Стоп-лосс в %'),
        ),
        migrations.AlterField(
            model_name='traid',
            name='result',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50, verbose_name='Результат $'),
        ),
    ]
