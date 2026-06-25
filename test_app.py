from backend.converter import convert


def test_convert_usd_to_eur():
    result = convert(1.1, "USD", "EUR")
    assert result == 1