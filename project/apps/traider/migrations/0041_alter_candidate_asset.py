# Generated by Django 3.2.8 on 2021-11-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0040_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='asset',
            field=models.CharField(max_length=50, verbose_name='Торговая пара'),
        ),
    ]