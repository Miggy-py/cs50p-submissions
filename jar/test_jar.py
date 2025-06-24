from jar import Jar
import pytest


def test_init():
    jar1 = Jar()
    jar2 = Jar(6)

    assert jar1.capacity == 12
    assert jar2.capacity == 6


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(4)
    with pytest.raises(ValueError):
        jar.deposit(10)

    assert jar.deposit(2) == 2


def test_withdraw():
    jar = Jar(6)
    jar.deposit(3)

    with pytest.raises(ValueError):
        jar.withdraw(4)

    assert jar.withdraw(2) == 1


def test_negative():
    with pytest.raises(ValueError):
        jar = Jar(-1)
