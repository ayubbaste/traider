# Generated by Django 3.2.8 on 2021-11-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0025_alter_deal_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='binance_id',
            field=models.IntegerField(editable=False, unique=True, verbose_name='Binance order ID'),
        ),
    ]
