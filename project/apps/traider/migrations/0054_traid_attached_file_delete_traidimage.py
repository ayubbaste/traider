# Generated by Django 4.0.1 on 2022-01-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0053_remove_traidimage_screenshot_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='traid',
            name='attached_file',
            field=models.ImageField(blank=True, upload_to='images/traids/', verbose_name='Screen shot'),
        ),
        migrations.DeleteModel(
            name='TraidImage',
        ),
    ]