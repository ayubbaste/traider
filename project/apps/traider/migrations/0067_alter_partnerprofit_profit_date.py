# Generated by Django 4.0.3 on 2022-08-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0066_alter_partnerprofit_profit_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerprofit',
            name='profit_date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]