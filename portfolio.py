class portfolio:
    def _init_(self):
        self._stock = []
    def buy(self, name, shares, price):
        self._stocks.append((name, shares, price))
    def cost(self):
        return sum(shares * price for name, shares, price in self._stocks)
        