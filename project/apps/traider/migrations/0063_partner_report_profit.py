# Generated by Django 4.0.3 on 2022-08-18 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0062_alter_traid_coin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Активен')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Имя')),
                ('percentage', models.DecimalField(decimal_places=4, default=0.0, max_digits=50, verbose_name='Доля в процентах от общего дохода')),
                ('note', models.TextField(blank=True, verbose_name='Заметка')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField(verbose_name='Дата отчета')),
                ('deposit', models.DecimalField(decimal_places=3, default=0, max_digits=20, verbose_name='Депозит в usdt')),
                ('gloabal_income', models.DecimalField(decimal_places=3, default=0, max_digits=20, verbose_name='Общая прибыль')),
                ('note', models.TextField(blank=True, verbose_name='Заметка')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='traider.partner', verbose_name='Партнер')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
                'ordering': ['-report_date'],
            },
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit_date', models.DateField(verbose_name='Дата')),
                ('income', models.DecimalField(decimal_places=3, default=0, max_digits=20, verbose_name='Прибыль')),
                ('note', models.TextField(blank=True, verbose_name='Заметка')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profits', to='traider.partner', verbose_name='Партнер')),
                ('report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profits', to='traider.report', verbose_name='Отчет')),
            ],
            options={
                'verbose_name': 'Полученная прибыль',
                'verbose_name_plural': 'Полученные прибыли',
                'ordering': ['-profit_date'],
            },
        ),
    ]
