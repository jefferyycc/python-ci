import re


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

    def calc(self, input):
        s = input
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = self.addition(self.multiply(num, 10), int(s[i]))
            if (not s[i].isdigit() and not s[i].isspace()) or i == self.decrement(len(s)):
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(self.multiply(stack.pop(), num))
                else:
                    tmp = stack.pop()
                    if self.division(tmp, num) < 0 and tmp % num != 0:
                        stack.append(self.increment(self.division(tmp, num)))
                    else:
                        stack.append(self.division(tmp, num))
                sign = s[i]
                num = 0
        return sum(stack)

    def isParenthesesValid(self, s):
        # if s is None: return True
        # elif (len(s) < 2): return False
        # else:
        s = s.replace(" ", "")
        print(s)
        dict = {")": "("}
        stack = []
        for char in s:
            print(char)
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            elif char.isdigit():
                print("meet digit")
                continue
            elif char == '+' or char == '-' or char == '*' or char == '/':
                print("meet symbol")
                continue
            # elif re.compile("[+\-*/]+").match(char):
            #     continue
            else:
                return False
        return stack == []

    def calc_p(self, input):
        if (self.isParenthesesValid(input) == True):
            s = input
            s = s + "$"

            def helper(stack, i):
                num = 0
                sign = '+'
                while i < len(s):
                    c = s[i]
                    if c == " ":
                        i = self.increment(i)
                        continue
                    if c.isdigit():
                        num = self.multiply(num, 10) + int(c)
                        i = self.increment(i)
                    elif c == '(':
                        num, i = helper([], i + 1)
                    else:
                        if sign == '+':
                            stack.append(num)
                        if sign == '-':
                            stack.append(-num)
                        if sign == '*':
                            stack.append(self.multiply(stack.pop(), num))
                        if sign == '/':
                            stack.append(self.division(int(stack.pop()), num))
                        num = 0
                        i = self.increment(i)
                        if c == ')':
                            return sum(stack), i
                        sign = c
                return sum(stack)

            return helper([], 0)
        else:
            raise ValueError
