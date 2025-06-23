from seasons import *
import pytest


def test_invalid_date():
    with pytest.raises(TypeError):
        minutes_since("1999", "10", "10")


def test_one_year_ago():
    assert minutes_since(2024,6,23) == 525600


def test_minutes_to_words():
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
