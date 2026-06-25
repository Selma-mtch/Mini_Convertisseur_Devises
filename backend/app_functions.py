import os

import requests
from dotenv import load_dotenv

load_dotenv()

rates = {
    "EUR": 1,
    "USD": 1.1,
    "JPY": 130,
    "GBP": 0.85,
    "CAD": 1.5,
}


def get_rates(api_key=None, base="EUR"):
    if api_key is None:
        api_key = os.environ.get("EXCHANGE_API_KEY", "")
    if not api_key:
        return rates
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
    try:
        data = requests.get(url, timeout=10).json()
        if data.get("result") == "success":
            return data["conversion_rates"]
    except requests.RequestException:
        pass
    return rates


def convert(amount, from_currency, to_currency, rates):
    if amount <= 0:
        return None
    if from_currency == to_currency:
        raise ValueError("Choisissez deux devises différentes.")
    return amount * rates[to_currency] / rates[from_currency]

def format_history(amount, from_currency, to_currency, result):
    return f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}"
