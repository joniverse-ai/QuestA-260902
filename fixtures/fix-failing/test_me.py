import pytest


def calculate_discount(price, rate):
    """Apply discount rate to price and return discounted price."""
    if rate < 0 or rate > 100:
        raise ValueError("Rate must be between 0 and 100")
    return price * (1 - rate / 100)


def merge_configs(base, override):
    """Merge override dict into base dict. Override wins on conflict."""
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result


# --- Tests ---

def test_discount_basic():
    assert calculate_discount(100, 10) == 90.0


def test_discount_zero_rate():
    # BUG: wrong expected value
    assert calculate_discount(200, 0) == 0


def test_discount_invalid_rate():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)


def test_merge_flat():
    base = {"a": 1, "b": 2}
    over = {"b": 3, "c": 4}
    assert merge_configs(base, over) == {"a": 1, "b": 3, "c": 4}


def test_merge_nested():
    base = {"db": {"host": "localhost", "port": 5432}}
    over = {"db": {"port": 3306}, "cache": True}
    # BUG: expected doesn't account for nested merge
    assert merge_configs(base, over) == {"db": {"port": 3306}, "cache": True}
