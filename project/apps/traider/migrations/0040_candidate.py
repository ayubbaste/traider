# Generated by Django 3.2.8 on 2021-11-13 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0039_auto_20211110_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeframe', models.CharField(blank=True, choices=[('1h', '1HOUR'), ('15min', '15MINUTES')], max_length=15, verbose_name='Time frame')),
                ('asset', models.CharField(max_length=50, unique=True, verbose_name='Торговая пара')),
                ('candidate_type', models.CharField(blank=True, choices=[('consoludatind', 'Поджатие'), ('breakingout', 'Пробитие')], max_length=15, verbose_name='Тип')),
                ('coin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='candidates', to='traider.coin', verbose_name='Монета')),
            ],
            options={
                'verbose_name': 'Кандидат',
                'verbose_name_plural': 'Кандидаты',
            },
        ),
    ]
