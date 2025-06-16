import pytest
from fuel import convert, gauge

def test_invalid_input():
    with pytest.raises(ValueError):
        convert("1")

    with pytest.raises(ValueError):
        convert("E")

    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_valid_inputs():
    assert convert("2/4") == 50
    assert convert("2/3") == 67
    assert convert("5/10") == 50


def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_gauge_on_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_regular():
    assert gauge(67) == "67%"
