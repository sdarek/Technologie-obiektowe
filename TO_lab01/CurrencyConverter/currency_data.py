from CurrencyConverter.currency import Currency
from CurrencyConverter.exchange_rate_provider import ExchangeRateProvider

class CurrencyData():

    def __init__(self, url):
        self.currencies = ExchangeRateProvider.download_currencies(url=url)
        self.url = url
        self.add_currency(Currency("Złoty Polski", 1, "PLN", 1.00))

    def add_currency(self, currency: Currency):
        self.currencies.append(currency)

    def update_currencies(self):
        self.__init__(self.url)

    def show_currencies(self, name=None, factor=None, code=True, exRate=None):
        for currency in self.currencies:
            output = ""
            if name:
                output += f"Nazwa waluty: {currency.get_name()} "
            if factor:
                output += f"Przelicznik: {currency.get_factor()} "
            if code:
                output += f"Kod waluty: {currency.get_code()} "
            if exRate:
                output += f"Kurs sredni: {currency.get_exchange_rate()} "

            print(output)