from CurrencyConverter.currency import Currency

class CurrencyData():

    def __init__(self):
        self.currencies = []

    def add_currency(self, currency: Currency):
        if currency not in self.currencies:
            self.currencies.append(currency)

    def get_currency_by_code(self, code):
        for currency in self.currencies:
            if currency.get_code() == code:
                return currency
        return None

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
