# Generated by Django 3.2.8 on 2021-10-22 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0022_alter_traid_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traid',
            name='result',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8, verbose_name='Результат'),
        ),
    ]
