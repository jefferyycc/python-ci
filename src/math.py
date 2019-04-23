class Math(object):
    def __init__(self):
        self.number_types = (int, float, complex)

    def increment(self, x):
        if isinstance(x, self.number_types):
            return x + 1
        else:
            raise ValueError

    def decrement(self, x):
        if isinstance(x, self.number_types):
            return x - 1
        else:
            raise ValueError

    def addition(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x + y
        else:
            raise ValueError

    def subtraction(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x - y
        else:
            raise ValueError

    def multiply(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x * y
        else:
            raise ValueError

    def division(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x / y
        else:
            raise ValueError
