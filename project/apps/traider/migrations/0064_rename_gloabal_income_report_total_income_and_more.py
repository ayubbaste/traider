# Generated by Django 4.0.3 on 2022-08-18 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0063_partner_report_profit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='gloabal_income',
            new_name='total_income',
        ),
        migrations.RemoveField(
            model_name='report',
            name='partner',
        ),
    ]