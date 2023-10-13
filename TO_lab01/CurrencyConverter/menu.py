from CurrencyConverter.currency_data import CurrencyData
from CurrencyConverter.currency_converter import CurrencyConverter
import os

class Menu():
    def __init__(self):
        os.system("clear")
        self.choice = None
        self.currencyData = CurrencyData("https://www.nbp.pl/kursy/xml/lasta.xml")
        self.converter = CurrencyConverter()
    
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
                os.system("clear")
                print("Nieprawidłowa opcja. Wybierz ponownie.")
    
    def make_decision(self):
        if self.choice == 1:
            os.system("clear")
            self.show_currencies()
        elif self.choice == 2:
            self.convert_currencies()
        elif self.choice == 3:
            os.system("clear")
            self.save_currencies()
        elif self.choice == 4:
            os.system("clear")
            self.update_currencies()
        elif self.choice == 5:
            os.system("clear")
            self.load_currencies_local()
        elif self.choice == 6:
            exit()
        else:
            os.system("clear")
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
            targetVal = self.converter.convert(sourceVal, sourceCode, targetCode, self.currencyData)
            os.system("clear")
            print(f"{sourceVal} {sourceCode} = {targetVal} {targetCode}")
        except ValueError as e:
            print(f"Błąd konwersji: {e}")


    def update_currencies(self):
        self.currencyData.update_currencies()

    def save_currencies(self):
        self.currencyData.save_currencies()

    def load_currencies_local(self):
        self.currencyData.load_currencies()

        

    
