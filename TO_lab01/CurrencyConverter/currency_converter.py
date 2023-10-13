from CurrencyConverter.currency_data import CurrencyData

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

    def convert(self, amount, sourceCode: str, targetCode: str, curData: CurrencyData):
        #Znajdź waluty na podstawie kodów źródłowego i docelowego
        source_currency = None
        target_currency = None

        for currency in curData.currencies:
            if currency.get_code() == sourceCode:
                source_currency = currency
            if currency.get_code() == targetCode:
                target_currency = currency

        if source_currency is None or target_currency is None:
            raise ValueError("Nie znaleziono odpowiednich walut")

        # Oblicz przeliczoną kwotę
        converted_amount = amount * (source_currency.get_exchange_rate() / target_currency.get_exchange_rate())
        return round(converted_amount, self.precision)