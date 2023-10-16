from CurrencyConverter.currency import Currency
from CurrencyConverter.exchange_rate_provider import ExchangeRateProvider
import pickle

class CurrencyData():

    def __init__(self, url):
        self.url = url
        self.filename = "currencies"
        self.update_currencies()

    def __init__(self, url):
        self.url = url
        self.filename = "currencies"
        self.currencies = ExchangeRateProvider.download_currencies(url=url)

    def add_currency(self, currency: Currency):
        if currency not in self.currencies:
            self.currencies.append(currency)

    def update_currencies(self):
        self.currencies = ExchangeRateProvider.download_currencies(self.url)
        self.add_currency(Currency("Złoty Polski", 1, "PLN", 1.00))
        print("Lista walut została zaktualizowana")
        

    def save_currencies(self):
        try:
            with open(self.filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Dane walut zostały zapisane do pliku: {self.filename}")
        except Exception as e:
            print(f"Błąd podczas zapisu danych walut: {e}")

    def load_currencies(self):
        try:
            with open(self.filename, 'rb') as file:
                loaded_data = pickle.load(file)
                self.currencies = loaded_data.currencies
            print(f"Lista walut została wczytana z pliku: {self.filename}")
        except Exception as e:
            print(f"Błąd podczas wczytywania walut z pliku: {e}")

    def show_currencies(self, name=None, factor=None, code=True, exRate=None):
        currency_info = []
        for currency in self.currencies:
            output = ""
            if name:
                output += f"{currency.get_name()} "
            if factor:
                output += f"{currency.get_factor()} "
            if code:
                output += f"{currency.get_code()} "
            if exRate:
                output += f"{currency.get_exchange_rate()} " 

            currency_info.append(output)

        # Łącz wszystkie informacje o walutach w jedną linię, oddzielając je separatorem " | "
        result = "| ".join(currency_info)
        print(result)
