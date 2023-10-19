import os
import json
import time
from decimal import Decimal
from datetime import date, datetime, timedelta
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager, BinanceSocketManager
# pip install python-dotenv
from dotenv import load_dotenv

from django.db import models
from datetime import datetime, date, time, timedelta
from django.utils.timesince import timesince


class Coin(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'
        ordering = ['name']

    def __str__(self):
        return self.name


class Reason(models.Model):
    name = models.CharField('Название', max_length=250, unique=True)
    note = models.TextField('Заметка', blank=True)

    class Meta:
        verbose_name = 'Основание'
        verbose_name_plural = 'Основания'
        ordering = ['name']

    def __str__(self):
        return self.name


class Indicator(models.Model):
    name = models.CharField('Название', max_length=250, unique=True)
    note = models.TextField('Заметка', blank=True)

    class Meta:
        verbose_name = 'Индикатор'
        verbose_name_plural = 'Индикаторы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Operation(models.Model):
    coin = models.ForeignKey(Coin, verbose_name='Монета',
                             related_name='operations',
                             on_delete=models.SET_NULL,
                             null=True, blank=True)
    binance_id = models.IntegerField('Order ID',editable=False,
                                     unique=True)
    operation_type = models.CharField('Тип', max_length=250, unique=False)
    operation_date = models.DateField('Дата')
    operation_time = models.TimeField('Время')
    qty = models.DecimalField('Кол-во', max_digits=50, decimal_places=4,
                              default=0.000)
    price = models.DecimalField('Цена', max_digits=50, decimal_places=4,
                                default=0.000)
    quoteQty = models.DecimalField('Сумма', max_digits=50, decimal_places=4,
                                   default=0.000)
    commission = models.DecimalField('Комиссия', max_digits=50, decimal_places=4,
                                     default=0.000)
    commissionAsset = models.CharField('Ком. вал.', max_length=250, unique=False)

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
        ordering = ['-operation_date']

    def __str__(self):
        return self.coin.name


class Traid(models.Model):
    coin = models.ForeignKey(Coin, verbose_name='Монета',
                             related_name='traids',
                             on_delete=models.SET_NULL,
                             null=True, blank=True)
    date = models.DateField('Дата', default=date.today,
                                       blank=True)
    time = models.TimeField('Время', auto_now_add=True,
                                     blank=True)
    buy_val = models.DecimalField('Объем покупки $', max_digits=50,
                                       decimal_places=2, default=0)
    sell_val = models.DecimalField('Объем продажи $', max_digits=50,
                                       decimal_places=2, default=0)
#    sell_perc_min = models.DecimalField('Минимальный процент продажи',
#                                        max_digits=8, decimal_places=4,
#                                        default=0.000)
#    sell_perc_max = models.DecimalField('Максимальный процент продажи',
#                                        max_digits=8, decimal_places=4,
#                                        default=0.000)
#    sell_perc_avg = models.decimalfield('средний процент продажи',
#                                        max_digits=8, decimal_places=4,
#                                        default=0, editable=false)
    result = models.DecimalField('Результат $', max_digits=50,
                                 decimal_places=2, default=0)
    result_percent = models.DecimalField('Результат в %', max_digits=50,
                                         decimal_places=2, default=0)
    stoploss_percent = models.DecimalField('Стоп-лосс в %', max_digits=50,
                                           decimal_places=2, default=0,
                                           blank=True)
    note = models.TextField('Заметка', blank=True)


    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
        ordering = ['-id']

    def __str__(self):
        return self.coin.name

    def save(self, *args, **kwargs):
#        # calculate deviders num
#        if self.sell_perc_min != 0 and self.sell_perc_max != 0:
#            num = 2
#        else:
#            num = 1
#        # calculate average sell percent
#        self.sell_perc_avg = (self.sell_perc_min + self.sell_perc_max) / num
#
#        # calculate trade result
#        self.result = self.position_val / 100 * self.sell_perc_avg
#

        load_dotenv()  # take environment variables from .env
        # pip install python-binance
        # https://python-binance.readthedocs.io/en/latest/overview.html
        client = Client(
            os.environ.get('BINANCE_API_KEY'),
            os.environ.get('BINANCE_API_SECRET'),
        )

        coin = self.coin.name

        # Get All Deals with the Coin
        deals = client.get_my_trades(symbol='%sUSDT' % coin)
        trades = {}
        num = 0

        for deal in deals:
            if not Operation.objects.filter(binance_id=deal['id']).exists():
                date = datetime.fromtimestamp(int(deal['time'])/1000)
                millis=deal['time']
                millis = int(millis)
                seconds=(millis/1000)%60
                seconds = int(seconds)
                minutes=(millis/(1000*60))%60
                minutes = int(minutes)
                hours=(millis/(1000*60*60))%24

                deal_date = date.date().strftime('%Y-%m-%d')
                deal_time = "%d:%d:%d" % (hours, minutes, seconds)

                if not deal['isBuyer']:
                    deal_type = 'Sell'
                else:
                    deal_type = 'Buy'

                num +=1

                trade = {"Trade #{}".format(num):[
                        deal['id'],
                        deal['symbol'],
                        deal_type,
                        deal_date,
                        deal_time,
                        deal['qty'],
                        deal['price'],
                        deal['quoteQty'],
                        deal['commission'],
                        deal['commissionAsset'],
                    ]
                }

                trades.update(trade)

                new_operation = Operation(
                        binance_id=deal['id'],
                        coin=self.coin,
                        operation_type=deal_type,
                        operation_date=deal_date,
                        operation_time=deal_time,
                        qty=deal['qty'],
                        price=deal['price'],
                        quoteQty=deal['quoteQty'],
                        commission=deal['commission'],
                        commissionAsset=deal['commissionAsset']
                )
                new_operation.save()
        else:
            pass

        buy_sum = 0
        sell_sum = 0

        for key, values in trades.items():
            if values[2] == "Buy":
                buy_sum = Decimal(buy_sum) + Decimal(values[7])
            elif values[2] == "Sell":
                sell_sum = Decimal(sell_sum) + Decimal(values[7])

        if buy_sum != 0:
            self.buy_val = buy_sum
            self.sell_val = sell_sum
            self.result = sell_sum - buy_sum
            self.result_percent = self.result / buy_sum * 100

        # save all data
        return super(Traid, self).save(*args, **kwargs)


class Screenshot(models.Model):
    traid = models.ForeignKey(Traid, on_delete=models.CASCADE,
                               verbose_name='сделка',
                               related_name='screenshots')

    filename = models.CharField('Filename', max_length=50, blank=True)
    attached_file = models.ImageField("Screen shot",
                                      upload_to='images/traids/',
                                      blank=True)
    class meta:
        verbose_name = 'Screenshot'
        verbose_name_plural = 'Screenshots'
        ordering = ['-filename']

    def __str__(self):
        return self.filename

    def update_filename(self, *args, **kwargs):
        self.filename = 'screenshot-n{}'.format(self.id)
        self.save()


class EntryReason(models.Model):
    traid = models.ForeignKey(Traid, on_delete=models.CASCADE,
                               verbose_name='сделка',
                               related_name='entry_reasons')
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE)


    class meta:
        verbose_name = 'Основание для входа'
        verbose_name_plural = 'Основания для входа'
        ordering = ['-reason__name']

    def __str__(self):
        return self.reason.name


class EntryIndicator(models.Model):
    traid = models.ForeignKey(Traid, on_delete=models.CASCADE,
                               verbose_name='сделка',
                               related_name='entry_indicator')
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)


    class meta:
        verbose_name = 'Примененный индикатор'
        verbose_name_plural = 'Примененные индикаторы'
        ordering = ['-indicator__name']

    def __str__(self):
        return self.indicator.name


class Balance(models.Model):
    date = models.DateTimeField('Время', default=datetime.now, blank=True)
    amount = models.DecimalField('Сумма', max_digits=8,
                                 decimal_places=2, default=0)
    currency = models.CharField('Валюта', max_length=50, blank=True)
    usd_equivalent = models.CharField('Эквивалент в USD', max_length=50, blank=True)
    note = models.TextField('Заметка', blank=True)

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Баланс'
        ordering = ['-date']

    def __int__(self):
        return self.pk


class Candidate(models.Model):
    TF_CHOICES = (
        ('4h', '4h'),
        ('1h', '1h'),
        ('30min', '30min'),
        ('15min', '15min'),
        ('5min', '5min'),
    )
    STATUS_CHOICES = (
        ('consoludating', 'Консолидация'),
        ('breakingout', 'Пробитие'),
    )
    timeframe = models.CharField('Time frame', max_length=15,
                    choices=TF_CHOICES, blank=True)
    symbol = models.CharField('Торговая пара', max_length=50)
    status = models.CharField('Статус', max_length=15,
                    choices=STATUS_CHOICES, blank=True)
    data = models.TextField('Candles data', blank=True)


    class Meta:
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"
        ordering = ['symbol']

    def __str__(self):
        return self.symbol
