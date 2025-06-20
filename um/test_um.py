from um import count


def test_none():
    assert count("yum") == 0
    assert count("yummy") == 0


def test_one():
    assert count("hello, um, world") == 1
    assert count("um...") == 1


def test_caps():
    assert count("UM") == 1
