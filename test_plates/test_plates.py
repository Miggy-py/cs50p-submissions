from plates import is_valid


def test_first_two_letters():
    assert is_valid("CSdf1") == True
    assert is_valid("lk504") == True
    assert is_valid("D5041") == False


def test_digits():
    assert is_valid("CSP50") == True
    assert is_valid("CS50P") == False


def test_empty():
    assert is_valid("") == False


def test_punc():
    assert is_valid("mL.50") == False
    assert is_valid("mL50.") == False


def test_size():
    assert is_valid("za") == True
    assert is_valid("abc123456") == False


def test_zero_location():
    assert is_valid("CS059") == False
