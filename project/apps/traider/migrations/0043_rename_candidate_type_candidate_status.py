# Generated by Django 3.2.8 on 2021-11-13 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0042_auto_20211113_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='candidate_type',
            new_name='status',
        ),
    ]