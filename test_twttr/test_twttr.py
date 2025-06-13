from twttr import shorten


def test_empty():
    assert shorten("") == ""


def test_numbers():
    assert shorten("1234") == "1234"


def test_case_vowels():
    assert shorten("BDaAeIooLkeS") == "BDLkS"


def test_punctuation():
    assert shorten("ptEdaH.pY") == "ptdH.pY"
