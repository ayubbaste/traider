# Generated by Django 3.2.8 on 2021-11-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0041_alter_candidate_asset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='asset',
            new_name='symbol',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='coin',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_type',
            field=models.CharField(blank=True, choices=[('consoludating', 'Поджатие'), ('breakingout', 'Пробитие')], max_length=15, verbose_name='Тип'),
        ),
    ]
