from my import my_unittest


def test_add():
    v = my_unittest.add(10, 20)
    assert v == 30


def test_menus():
    v = my_unittest.menus(60, 20)
    assert v == 40


def test_product():
    v = my_unittest.product(6, 2)
    assert v == 12


def test_division_ok():
    v = my_unittest.division(60, 20)
    assert v == 3


def test_division_zero():
    v = my_unittest.division(60, 0)
    assert v == 0