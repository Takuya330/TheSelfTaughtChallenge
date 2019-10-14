def add_mult(a, b, c, x=50, y=10):
    """ Returns the result of two optional params
    multipled by the addition of 3 required params.
    :param a: int.
    :param b: int.
    :param c: int.
    :param x: int.
    :param y: int.
    :return: int.
    """
    return a + b + c * x * y

result = add_mult(10, 20, 30)
print(result)
