# Generated by Django 4.0.3 on 2022-08-22 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0064_rename_gloabal_income_report_total_income_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerProfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit_date', models.DateField(verbose_name='Дата')),
                ('profit', models.DecimalField(decimal_places=3, default=0, max_digits=20, verbose_name='Прибыль')),
                ('note', models.TextField(blank=True, verbose_name='Заметка')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profits', to='traider.partner', verbose_name='Партнер')),
            ],
            options={
                'verbose_name': 'Прибыль',
                'verbose_name_plural': 'Прибыль',
                'ordering': ['-profit_date'],
            },
        ),
        migrations.RenameField(
            model_name='report',
            old_name='total_income',
            new_name='income',
        ),
        migrations.DeleteModel(
            name='Profit',
        ),
    ]
