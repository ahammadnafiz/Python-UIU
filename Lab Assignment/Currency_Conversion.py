import json
import os

file_name = 'currency.txt'

def load_currency(file_name):
    try:
        with open(file_name, 'r') as data:
            content = data.read()
        return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error Loading File: {e}')
        

def save_currency(local, choice, rate, filename='conversion.txt', file_name='currency.txt'):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    key = f"{local} to {choice}"
    data[key] = rate

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def currency_conversion(local, choice, data):
    # Check if the target currency exists in the data dictionary
    if choice in data:
        exchange_rate = data[choice]
        result = local * exchange_rate
        return result


def show_conversion(local, choice, filename='conversion.txt'):
    data = load_currency(filename)
    if data:
        key = f"{local} to {choice}"
        if key in data:
            print(f"{local} BDT to {choice.upper()} is: {data[key]} {choice.upper()}")
        else:
            print(f"No conversion data found for {local} to {choice}")
    else:
        print("No conversion data found.")
            
def main():
    currency = load_currency(file_name)
    
    local = float(input('Enter an amount (BDT) for Conversion: '))
    
    while True:
        print("Currency Selection:")
        print("1. USD - US Dollar")
        print("2. EUR - Euro")
        print("3. GBP - British Pound")
        print("4. CAD - Canadian Dollar")
        print("5. AUD - Australian Dollar")
        print("6. CHF - Swiss Franc")
        print("7. DKK - Danish Krone")
        print("8. NOK - Norwegian Krone")
        print("9. SEK - Swedish Krona")
        print("10. AED - United Arab Emirates Dirham")
        print("11. Exit")
        
        choice = input("Enter the number of the currency you want to convert to: ")
        
        if choice == '1':
            result = currency_conversion(local, 'usd', currency)
            save_currency(local, 'usd', result)
            show_conversion(local, 'usd')
        elif choice == '2':
            result = currency_conversion(local, 'eur', currency)
            save_currency(local, 'eur', result)
            show_conversion(local, 'eur')
        elif choice == '3':
            result = currency_conversion(local, 'gbp', currency)
            save_currency(local, 'gbp', result)
            show_conversion(local, 'gbp')
        elif choice == '4':
            result = currency_conversion(local, 'cad', currency)
            save_currency(local, 'cad', result)
            show_conversion(local, 'cad')
        elif choice == '5':
            result = currency_conversion(local, 'aud', currency)
            save_currency(local, 'aud', result)
            show_conversion(local, 'aud')
        elif choice == '6':
            result = currency_conversion(local, 'chf', currency)
            save_currency(local, 'chf', result)
            show_conversion(local, 'chf')
        elif choice == '7':
            result = currency_conversion(local, 'dkk', currency)
            save_currency(local, 'dkk', result)
            show_conversion(local, 'dkk')
        elif choice == '8':
            result = currency_conversion(local, 'nok', currency)
            save_currency(local, 'nok', result)
            show_conversion(local, 'nok')
        elif choice == '9':
            result = currency_conversion(local, 'sek', currency)
            save_currency(local, 'sek', result)
            show_conversion(local, 'sek')
        elif choice == '10':
            result = currency_conversion(local, 'aed', currency)
            save_currency(local, 'aed', result)
            show_conversion(local, 'aed')
        elif choice == '11':
            print('Goodbye')
            save_currency(local, choice, result)
            break
        else:
            print('Please enter a valid action')
            
            
if __name__ == '__main__':
    main()