# Generated by Django 3.2.8 on 2021-10-10 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='end_end',
            new_name='end_time',
        ),
    ]
