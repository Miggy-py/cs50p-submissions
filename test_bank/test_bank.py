from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0


def test_starts_with_h():
    assert value("hamburger") == 20
    assert value("Harold") == 20


def test_other_greeting():
    assert value("whats up") == 100
    assert value("Whats up") == 100


def test_numbers():
    assert value("1234") == 100


def test_empty():
    assert value("") == 100
