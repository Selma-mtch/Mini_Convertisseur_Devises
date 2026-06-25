rates = {
    "EUR": 1,
    "USD": 1.1,
    "JPY": 130,
}


def convert(amount, from_currency, to_currency, rates):
    if amount <= 0:
        return None
    if from_currency == to_currency:
        raise ValueError("Choisissez deux devises différentes.")
    return amount * rates[to_currency] / rates[from_currency]
