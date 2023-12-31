# Generated by Django 4.0.3 on 2022-08-22 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0065_partnerprofit_rename_total_income_report_income_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerprofit',
            name='profit_date',
            field=models.DateField(unique=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_date',
            field=models.DateField(unique=True, verbose_name='Дата отчета'),
        ),
    ]
