# Generated by Django 3.2.8 on 2021-11-03 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0029_auto_20211103_2310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='traid',
            options={'ordering': ['-date'], 'verbose_name': 'Сделка', 'verbose_name_plural': 'Сделки'},
        ),
        migrations.RemoveField(
            model_name='traid',
            name='number',
        ),
    ]
