from numb3rs import validate


def test_only_first():
    assert validate("12.278.890.756") == False


def test_too_big():
    assert validate("256.256.256.256") == False


def test_non_numbers():
    assert validate("E.d.a.L") == False


def test_no_numbers():
    assert validate("....") == False


def test_test_trailing():
    assert validate("d 5.5.5.5 e") == False


def test_valid_ip():
    assert validate("5.5.5.5") == True
    assert validate("123.45.6.78") == True
