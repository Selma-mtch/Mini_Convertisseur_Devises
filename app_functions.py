# app_functions.py
def convert(amount, from_currency, to_currency, rates):
    if amount <= 0:
        return None
    if from_currency == to_currency:
        return amount
    return amount * rates[to_currency] / rates[from_currency]
