from locale import currency
from turtle import update
from CurrencyConverter.exchange_rate_provider import ExchangeRateProvider
from CurrencyConverter.currency import Currency
from CurrencyConverter.currency_data import CurrencyData
import pickle

class DataOperations():
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        
    def update_currencies(self, currency_data: CurrencyData):
        try:
            # Wywołaj funkcję z klasy ExchangeRateProvider do pobrania aktualnych kursów walut
            updated_currencies = ExchangeRateProvider.download_currencies(self.url)
            currency_data.currencies = updated_currencies
            currency_data.add_currency(Currency("Złoty Polski", 1, "PLN", 1.00))
            print(f"Lista walut została zaktualizowana")
        except Exception as e:
            print(f"Błąd podczas aktualizacji walut: {e}")
        

    def save_currencies(self, currency_data: CurrencyData):
        try:
            with open(self.filename, 'wb') as file:
                pickle.dump(currency_data.currencies, file)
            print(f"Dane walut zostały zapisane do pliku: {self.filename}")
        except Exception as e:
            print(f"Błąd podczas zapisu danych walut: {e}")

    def load_currencies(self):
        try:
            with open(self.filename, 'rb') as file:
                loaded_data = pickle.load(file)
                return loaded_data
        except Exception as e:
            print(f"Błąd podczas wczytywania walut z pliku: {e}")
            return []