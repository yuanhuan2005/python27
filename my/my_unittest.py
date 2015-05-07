def add(a, b):
    return a + b


def menus(a, b):
    return a - b


def product(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
