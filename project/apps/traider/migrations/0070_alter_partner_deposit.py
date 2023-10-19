# Generated by Django 4.0.3 on 2023-02-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0069_alter_partnerprofit_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='deposit',
            field=models.DecimalField(decimal_places=4, default=models.DecimalField(decimal_places=4, default=0.0, max_digits=50, verbose_name='Начальный депозит партнера'), max_digits=50, verbose_name='Текущий депозит партнера'),
        ),
    ]
