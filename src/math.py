class Math():
    def addition(x, y):
        if not isinstance(x, int) and not isinstance(y, int):
            return 'Invalid input'
        else:
            return x + y
