from CurrencyConverter.currency_data import CurrencyData
from CurrencyConverter.currency_converter import CurrencyConverter
from CurrencyConverter.data_operations import DataOperations
import os

class Menu():
    def __init__(self):
        os.system("cls")
        self.choice = None
        self.currencyData = CurrencyData()
        self.converter = CurrencyConverter()
        self.dataOper = DataOperations("https://www.nbp.pl/kursy/xml/lasta.xml", "currencies")
    
    def show_menu(self):

        while self.choice != 6:
            print('----------------------MENU-------------------')
            print('1. Wyświetl kody dostępnych walut')
            print('2. Konwertuj')
            print('3. Zapisz listę walut lokalnie')
            print('4. Wczytaj listę walut z sieci')
            print('5. Wczytaj waluty z komputera')
            print('6. Koniec\n')
            try:
                self.choice = int(input("Twój wybór: "))
                self.make_decision()
            except ValueError:
                os.system("cls")
                print("Nieprawidłowa opcja. Wybierz ponownie.")
    
    def make_decision(self):
        if self.choice == 1:
            os.system("cls")
            self.show_currencies()
        elif self.choice == 2:
            self.convert_currencies()
        elif self.choice == 3:
            os.system("cls")
            self.save_currencies()
        elif self.choice == 4:
            os.system("cls")
            self.update_currencies()
        elif self.choice == 5:
            os.system("cls")
            self.load_currencies_local()
        elif self.choice == 6:
            exit()
        else:
            os.system("cls")
            print("Nieprawidłowa opcja. Wybierz ponownie.")

    def show_currencies(self):
        show_names = str(input("Wyświetlać pełne nazwy walut? (tak/nie): "))
        if (show_names == "tak"):
            show_names = True
        elif (show_names == "nie"):
            show_names = False
        else:
            show_names = False
        self.currencyData.show_currencies(name = show_names, factor = False, code = True, exRate = False)
    
    def convert_currencies(self):
        sourceVal = float(input("Podaj wartość początkową [float]: "))
        sourceCode = str(input("Podaj kod waluty początkowej [str]: ")).upper()
        targetCode = str(input("Podaj kod waluty docelowej [str]: ")).upper()
        try:
            sourceCurrency = self.currencyData.get_currency_by_code(sourceCode)
            targetCurrency = self.currencyData.get_currency_by_code(targetCode)

            if sourceCurrency is None or targetCurrency is None:
                os.system("cls")
                print("Nieprawidłowe kody walut. Spróbuj ponownie.")
            else:
                convertedValue = self.converter.convert(sourceVal, sourceCurrency, targetCurrency)
                os.system("cls")
                print(f"{sourceVal} {sourceCode} = {convertedValue} {targetCode}")
        except ValueError as e:
            os.system("cls")
            print(f"Błąd konwersji: {e}")

    def update_currencies(self):
        self.dataOper.update_currencies(self.currencyData)

    def save_currencies(self):
        self.dataOper.save_currencies(self.currencyData)

    def load_currencies_local(self):
        self.currencyData.currencies = self.dataOper.load_currencies()

        

    
