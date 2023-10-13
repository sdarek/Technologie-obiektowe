class Currency:
    def __init__(self, name, factor, code, exchangeRate):
        self.name = name  # Pełna nazwa waluty, np. "US Dollar"
        self.factor = factor  # Współczynnik przeliczeniowy, np. 1 (dla większości walut)
        self.code = code  # Kod waluty, np. "USD"
        self.exchangeRate = exchangeRate  # Aktualny kurs wymiany

    def get_name(self):
        return self.name

    def get_factor(self):
        return self.factor

    def get_code(self):
        return self.code

    def get_exchange_rate(self):
        return self.exchangeRate

    def set_exchange_rate(self, exchangeRate):
        self.exchangeRate = exchangeRate
