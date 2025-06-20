from working import convert
import pytest


def test_valids():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_invalid_delimiter():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
