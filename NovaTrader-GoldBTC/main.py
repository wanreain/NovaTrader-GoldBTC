import time
from btc_trading import BinanceTrader
from gold_price import GoldPriceFetcher
from strategy import Strategy
from telegram_bot import send_telegram_message

trader = BinanceTrader()
gold = GoldPriceFetcher()
strategy = Strategy()

while True:
    btc_price = trader.get_current_price()
    gold_price = gold.get_current_price()
    signal = strategy.generate_signal(btc_price)

    if signal == "BUY":
        trader.buy()
        send_telegram_message("BTC Buy signal executed.")
    elif signal == "SELL":
        trader.sell()
        send_telegram_message("BTC Sell signal executed.")

    time.sleep(60)