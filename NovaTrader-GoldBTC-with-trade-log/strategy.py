class Strategy:
    def __init__(self):
        self.prices = []

    def generate_signal(self, price):
        self.prices.append(price)
        if len(self.prices) > 20:
            short = sum(self.prices[-5:]) / 5
            long = sum(self.prices[-20:]) / 20
            if short > long:
                return "BUY"
            elif short < long:
                return "SELL"
        return "HOLD"