def suma(x, y):
    return x + y


def dif(x, y):
    return x - y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "You can't divide by 0"


def multiple(x, y):
    return x * y
