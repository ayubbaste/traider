# Generated by Django 3.2.8 on 2021-11-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0046_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='traid',
            name='result_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50, verbose_name='Результат в %'),
        ),
    ]