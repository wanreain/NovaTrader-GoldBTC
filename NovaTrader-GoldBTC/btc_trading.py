import requests
import os
import csv
from datetime import datetime

class BinanceTrader:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.position = None

    def get_current_price(self):
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        return float(r.json()["price"])

    def buy(self):
        self.position = "LONG"
        self.log_trade("BUY")

    def sell(self):
        self.position = None
        self.log_trade("SELL")

    def log_trade(self, action):
        with open("trade_log.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), action])