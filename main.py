# Currency converter
# Joao Pedro Costa
# This is a simple program to convert currencies, using an API to convert it in real-time.

from forex_python.converter import CurrencyRates as CurrencyRatesClass

def Interface():
    print("Welcome to Currency Converter!\n")

    # Using the forex-python library to get a list of currency codes
    currency_rates_instance = CurrencyRatesClass()
    # Using "USD" as the base currency
    currency_codes = currency_rates_instance.get_rates("USD")

    for code in currency_codes:
        # These for prints all the currency codes
        print("current currency code: " + code)

    currency1, currency2 = input("What would you like to convert: ").split(" ")
    
    currency1 = currency1.upper()
    currency2 = currency2.upper()
    
    # Here takes the currency code and converts it to the desired currency
    print(currency_rates_instance.convert(currency1, currency2, 1))
    
    

def main():
    while True:
        Interface()
        print("Would you like to continue? (y/n)")
        if input().lower() == "y":
            continue
        else:
            break

main()
