import requests
from bs4 import BeautifulSoup
from CurrencyConverter.currency import Currency

class ExchangeRateProvider():

    @staticmethod
    def download_currencies(url):
        try:
            response = requests.get(url)  # Pobieramy zawartość strony z kursami walut
            response.raise_for_status()  # Rzuć wyjątek w przypadku problemów z zapytaniem HTTP
            soup = BeautifulSoup(response.text, features="xml")
            table = soup.find('tabela_kursow')  # Znajdź odpowiednią tabelę

            if table:
                currencies = []
                # Iterujemy przez pozycje w tabeli i znajdujemy odpowiednią walutę
                for pozycja in table.find_all('pozycja'):
                    name = pozycja.find('nazwa_waluty').text
                    factor = pozycja.find('przelicznik').text
                    code = pozycja.find('kod_waluty').text
                    exchangeRate = float(pozycja.find('kurs_sredni').text.replace(',', '.'))
                    currencies.append(Currency(name, factor, code, exchangeRate))
                print(f"Lista walut została pobrana ze strony {url}")
                return currencies
        except requests.RequestException as exc:
            raise Exception(f"Błąd zapytania HTTP: {exc}")