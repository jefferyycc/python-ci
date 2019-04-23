class Math(object):
    def increment(self):
        return self + 1

    def decrement(self):
        return self - 1

    def addition(x, y):
        number_types = (int, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
        return x + y