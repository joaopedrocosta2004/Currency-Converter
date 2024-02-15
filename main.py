# Currency converter
# Joao Pedro Costa
# This is a simple program to convert currencies, using an API to convert it in real-time.

from forex_python.converter import CurrencyRates as CurrencyRatesClass


def get_valid_currency_codes():
    # Using the forex-python library to get a list of currency codes
    currency_rates_instance = CurrencyRatesClass()
    currency_codes = currency_rates_instance.get_rates("THB")
    return currency_codes


def print_currency_codes(currency_codes):
    print("Available currency codes:")
    for code in currency_codes:
        print(code)


def get_user_input(currency_codes):
    while True:
        print_currency_codes(currency_codes)
        user_input = input("Enter two currency codes separated by space: ").split()
        if len(user_input) != 2:
            print("Please enter two currency codes separated by a space.")
            continue
        currency1, currency2 = user_input
        currency1 = currency1.upper()
        currency2 = currency2.upper()
        if currency1 not in currency_codes or currency2 not in currency_codes:
            print("Invalid currency code! Please try again.")
            continue
        return currency1, currency2


def convert_currency(currency_rates_instance, currency1, currency2):
    amount = float(input(f"Enter amount in {currency1}: "))
    converted_amount = currency_rates_instance.convert(currency1, currency2, amount)
    print(f"{amount} {currency1} is equal to {converted_amount:.2f} {currency2}")


def main():
    print("Welcome to Currency Converter!\n")
    currency_codes = get_valid_currency_codes()
    while True:
        currency1, currency2 = get_user_input(currency_codes)
        convert_currency(CurrencyRatesClass(), currency1, currency2)
        choice = input("Would you like to continue? (y/n): ")
        if choice.lower() != "y":
            break


if __name__ == "__main__":
    main()
