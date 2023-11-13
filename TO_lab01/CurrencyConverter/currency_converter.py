from CurrencyConverter.currency import Currency
from decimal import Decimal


class CurrencyConverter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CurrencyConverter, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.precision = 2  # Domyślna precyzja

    def set_precision(self, precision):
        self.precision = precision

    def convert(self, amount, sourceCur: Currency, targetCur: Currency):
        # Oblicz przeliczoną kwotę z użyciem modułu decimal
        source_exchange_rate = sourceCur.get_exchange_rate()
        target_exchange_rate = targetCur.get_exchange_rate()
        amount = Decimal(str(amount))
        converted_amount = (amount * Decimal(source_exchange_rate)) / Decimal(target_exchange_rate)
        return round(converted_amount, self.precision)