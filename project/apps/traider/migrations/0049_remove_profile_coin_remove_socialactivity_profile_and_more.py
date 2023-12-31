# Generated by Django 4.0.1 on 2022-01-30 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traider', '0048_traid_stoploss_percent_alter_traid_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='coin',
        ),
        migrations.RemoveField(
            model_name='socialactivity',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='socialactivity',
            name='socialnetwork',
        ),
        migrations.RemoveField(
            model_name='tradesonexchange',
            name='exchange',
        ),
        migrations.RemoveField(
            model_name='tradesonexchange',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='attached_file',
            field=models.ImageField(blank=True, upload_to='images/traids/', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='traid',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='traider.image', verbose_name='Image'),
        ),
        migrations.DeleteModel(
            name='ActiveInvestor',
        ),
        migrations.DeleteModel(
            name='Exchange',
        ),
        migrations.DeleteModel(
            name='Investor',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='SocialActivity',
        ),
        migrations.DeleteModel(
            name='SocialNetwork',
        ),
        migrations.DeleteModel(
            name='TradesOnExchange',
        ),
    ]
