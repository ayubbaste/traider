# Generated by Django 3.2.8 on 2021-10-13 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0012_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='position_val',
        ),
        migrations.AddField(
            model_name='balance',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Сумма'),
        ),
    ]
