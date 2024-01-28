# Currency converter
# Joao Pedro Costa
# This is a simple program to convert currencies, using an API to convert it in real-time.

from forex_python.converter import CurrencyRates as CurrencyRatesClass

def Interface():

    # Using the forex-python library to get a list of currency codes
    currency_rates_instance = CurrencyRatesClass()
    # Using "USD" as the base currency
    currency_codes = currency_rates_instance.get_rates("THB")

    for code in currency_codes:
        # These for prints all the currency codes
        print("current currency code: " + code)

    user_input = input("What would you like to convert: ").split()
    if len(user_input) != 2:
        print("Please enter two currency codes separated by a space.")
        return
    currency1, currency2 = user_input
    
    currency1 = currency1.upper()
    currency2 = currency2.upper()
    
    if currency1 not in currency_codes or currency2 not in currency_codes and currency1 != "THB" or currency2!= "THB":
        print("Invalid currency code!")
        return
    

    # Here takes the currency code and converts it to the desired currency
    print(currency_rates_instance.convert(currency1, currency2, 1))
    
    

def main():
    print("Welcome to Currency Converter!\n")
    while True:
        Interface()
        print("Would you like to continue? (y/n)")
        if input().lower() == "y":
            continue
        else:
            break

main()
