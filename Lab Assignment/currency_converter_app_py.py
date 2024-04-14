import json
import requests
from bs4 import BeautifulSoup
import streamlit as st
import datetime

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


def scrape_xe_exchange_rates():
    url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the exchange rate
            exchange_rate_element = soup.find('span', {'class': 'converterresult-toAmount'})
            exchange_rate = exchange_rate_element.text.strip()

            return exchange_rate

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def currency_conversion(local, choices, data):
    converted_currencies = {}
    for choice in choices:
        if choice in data:
            exchange_rate = data[choice]
            result = local * exchange_rate
            converted_currencies[choice] = result
        else:
            print(f"No conversion data found for {local} to {choice}")

    return converted_currencies


def main():
    currency = load_currency(file_name)

    st.title("Currency Converter App")

    local = st.number_input('Enter an amount (BDT) for Conversion:', value=1.0)

    currency_input = st.text_input("Enter the currencies you want to convert to (comma-separated, e.g., usd,eur,aed):")
    choices = [choice.strip().lower() for choice in currency_input.split(',')]

    if st.button("Convert"):
        converted_currencies = currency_conversion(local, choices, currency)
        for choice, result in converted_currencies.items():
            st.write(f"{local} BDT to {choice.upper()} is: {result} {choice.upper()}")

        another_conversion = st.radio("Do you want to convert a different value?", ['Yes', 'No'])
        if another_conversion == 'No':
            st.success('Goodbye!')


if __name__ == '__main__':
    main()
