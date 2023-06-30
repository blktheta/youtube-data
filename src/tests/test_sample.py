import src.sample


def test_square():
    assert src.sample.square(5) == 25


def test_square_float():
    assert src.sample.square(3.0) == 9.0
