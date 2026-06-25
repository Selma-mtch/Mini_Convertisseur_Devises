from backend.app_functions import rates, convert, format_history

def test_convert_usd_to_eur():
    result = convert(11, "USD", "EUR", rates)
    assert result == 10



def test_convert_eur_to_usd():
    result = convert(10, "EUR", "USD", rates)
    assert result == 11




def test_convert_returns_none_when_amount_is_zero():
    result = convert(0, "EUR", "USD", rates)
    assert result is None


def test_convert_returns_none_when_amount_is_negative():
    result = convert(-5, "EUR", "USD", rates)
    assert result is None

def test_convert_with_zero_amount_returns_none():
    result = convert(0, "EUR", "USD", rates)
    assert result is None


def test_convert_with_negative_amount_returns_none():
    result = convert(-5, "EUR", "USD", rates)
    assert result is None


def test_convert_same_currency_raises_value_error():
    with pytest.raises(ValueError):
        convert(10, "EUR", "EUR", rates)


def test_format_history():
    result = format_history(10, "EUR", "USD", 11)
    assert result == "10.00 EUR = 11.00 USD"