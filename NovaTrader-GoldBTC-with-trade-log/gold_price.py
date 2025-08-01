import requests
import os

class GoldPriceFetcher:
    def __init__(self):
        self.api_key = os.getenv("GOLD_API_KEY")

    def get_current_price(self):
        headers = {'x-access-token': self.api_key}
        r = requests.get("https://www.goldapi.io/api/XAU/USD", headers=headers)
        return r.json()["price"]