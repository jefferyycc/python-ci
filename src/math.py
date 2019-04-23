class Math(object):
    def increment(x):
        number_types = (int, float, complex)
        if isinstance(x, number_types):
            return x + 1
        else:
            raise ValueError

    def decrement(x):
        number_types = (int, float, complex)
        if isinstance(x, number_types):
            return x - 1
        else:
            raise ValueError

    def addition(x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
