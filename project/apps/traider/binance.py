import os
import time
import json
from datetime import datetime
from traider.models import *
# pip install python-dotenv
from dotenv import load_dotenv
# Binance API
# pip install python-binance
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager, BinanceSocketManager


def scan(timeframe):
        load_dotenv()  # take environment variables from .env
        # pip install python-binance
        # https://python-binance.readthedocs.io/en/latest/overview.html
        client = Client(
            os.environ.get('BINANCE_API_KEY'),
            os.environ.get('BINANCE_API_SECRET'),
        )

        for coin in Coin.objects.all():
            symbol = "%sUSDT" % coin
            timeframe = timeframe

            try:
                Candidate.objects.get(symbol=symbol, timeframe=timeframe).delete()
            except:
                pass

            if timeframe=="4h":
                klines = client.get_historical_klines(
                    symbol,Client.KLINE_INTERVAL_4HOUR, "15 day ago UTC"
                )
            if timeframe=="1h":
                klines = client.get_historical_klines(
                    symbol,Client.KLINE_INTERVAL_1HOUR, "15 day ago UTC"
                )
            elif timeframe=="30min":
                klines = client.get_historical_klines(
                    symbol,Client.KLINE_INTERVAL_30MINUTE, "15 day ago UTC"
                )
            elif timeframe=="15min":
                klines = client.get_historical_klines(
                    symbol,Client.KLINE_INTERVAL_15MINUTE, "15 day ago UTC"
                )
            elif timeframe=="5min":
                klines = client.get_historical_klines(
                    symbol,Client.KLINE_INTERVAL_5MINUTE, "15 day ago UTC"
                )

            candles_close_data = []

            for i in klines:
                #date = datetime.fromtimestamp(int(i[0])/1000)
                #date = date.date().strftime('%d.%m.%Y')
                #print(date)
                candles_close_data.append(i[4])

            def is_consolidating(candles_close_data, percentage=0.3):
                last_candles_data = candles_close_data[-11:]
                max_close = max(last_candles_data)
                min_close = min(last_candles_data)
                threshold = 1 - (percentage / 100)


                if float(min_close) > (float(max_close) * threshold):
                    Candidate.objects.create(
                        symbol = symbol,
                        timeframe = timeframe,
                        data = last_candles_data,
                        status = "Консолидация"
                    )


            def is_breaking_out(candles_close_data, percentage=0.3):
                last_close = candles_close_data[-1]

                if is_consolidating(candles_close_data[:-1], percentage=percentage):
                    recent_closes = candles_close_data[-10:-1]

                    if last_close > max(recent_closes):
                        Candidate.objects.create(
                            symbol = symbol,
                            timeframe = timeframe,
                            data = recent_closes,
                            status = "Пробитие"
                        )

            #time.sleep(2)

            is_breaking_out(candles_close_data)

