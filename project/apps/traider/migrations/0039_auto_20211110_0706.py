# Generated by Django 3.2.8 on 2021-11-10 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0038_auto_20211107_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Название')),
                ('note', models.TextField(blank=True, verbose_name='Заметка')),
            ],
            options={
                'verbose_name': 'Индикатор',
                'verbose_name_plural': 'Индикаторы',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='entryreason',
            options={},
        ),
        migrations.AlterField(
            model_name='entryreason',
            name='traid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_reasons', to='traider.traid', verbose_name='сделка'),
        ),
        migrations.CreateModel(
            name='EntryIndicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traider.indicator')),
                ('traid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_indicator', to='traider.traid', verbose_name='сделка')),
            ],
        ),
    ]