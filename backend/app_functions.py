rates = {
    "EUR": 1,
    "USD": 1.1,
    "JPY": 130
}

def convert(amount, from_currency, to_currency):
    return amount * rates[to_currency] / rates[from_currency]

