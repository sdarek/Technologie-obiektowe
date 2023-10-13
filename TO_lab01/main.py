from CurrencyConverter.currency import Currency
from CurrencyConverter.currency_converter import CurrencyConverter
from CurrencyConverter.currency_data import CurrencyData


if __name__ == "__main__":
    converter = CurrencyConverter()
    currencyData = CurrencyData("https://www.nbp.pl/kursy/xml/lasta.xml")

    currencyData.update_currencies()
    currencyData.show_currencies(name=True, factor=None, code=True, exRate=None)

    amount = 100

    sourceCur = Currency("Dolar Amerykański", 1, "USD", 1.4)
    targetCur = Currency("Złoty Polski", 10, "THB", 1.3)


    try:
        result = converter.convert(amount, sourceCur, targetCur)
        print(f"{amount} {sourceCur.code} = {result} {targetCur.code}")
    except Exception as e:
        print(f"Błąd: {e}")
