from CurrencyConverter.currency import Currency

class CurrencyConverter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CurrencyConverter, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.precision = 2  # Domyślna precyzja
        self.exchangeRateProvider = None  # Domyślnie brak dostawcy kursów walut

    def set_precision(self, precision):
        self.precision = precision

    def set_exchange_rate_provider(self, provider):
        self.exchangeRateProvider = provider

    def convert(self, amount, source_currency: Currency, target_currency: Currency):
        if not self.exchangeRateProvider:
            raise ValueError("Brak dostawcy kursów walut.")

        source_rate = self.exchangeRateProvider.get_exchange_rate(source_currency.get_code())
        target_rate = self.exchangeRateProvider.get_exchange_rate(target_currency.get_code())

        if source_rate is None:
            raise ValueError(f"Brak kursu dla waluty źródłowej: {source_currency}")
        if target_rate is None:
            raise ValueError(f"Brak kursu dla waluty docelowej: {target_currency}")

        converted_amount = amount * (target_rate / source_rate)
        return round(converted_amount, self.precision)
