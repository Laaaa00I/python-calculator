import math


class Operation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self):
        raise NotImplementedError

    def __str__(self):
        return str(self.calculate())
#^^^ This is parent class

class Sum(Operation):
    def calculate(self):
        return self.x + self.y
#^^^ This is addition operation (x + y)

class Mult(Operation):
    def calculate(self):
        return self.x * self.y
#^^^ This is multiplication operation (x * y)

class Div(Operation):
    def calculate(self):
        if self.y == 0:
            raise ZeroDivisionError("division by zero")
        return self.x / self.y
#^^^ This is division operation (x / y), takes into account division by zero

class Sub(Operation):
    def calculate(self):
        return self.x - self.y
#^^^ This is subtraction operation (x - y)

class Pow(Operation):
    def calculate(self):
        if self.x == 0 and self.y < 0:
            raise ZeroDivisionError("cannot raise 0 to a negative power")
        try:
            return self.x ** self.y
        except OverflowError:
            raise OverflowError("result is too large!")
#^^^ This is exponentiation operation (x ** y), takes into account the raising of zero to a negative power and buffer overflow

class Root(Operation):
    def calculate(self):
        import math
        if self.y == 0:
            raise ZeroDivisionError("degree of the root cannot be zero")
        if self.x < 0 and self.y % 2 == 0:
            raise ZeroDivisionError("even root of a negative number")
        if self.x < 0:
            return -math.exp(math.log(abs(self.x)) / self.y)
        return math.exp(math.log(self.x) / self.y)
#^^^ This is root calculation operation (x ** (1 / y)), takes into account degree of the root and even root of a negative number

class Sin(Operation):
    def calculate(self):
        return math.sin(self.x)
#^^^ This is sin operation (sin x)

class Cos(Operation):
    def calculate(self):
        return math.cos(self.x)
#^^^ This is cos operation (cos x)

class Tan(Operation):
    def calculate(self):
        return math.tan(self.x)
#^^^ This is tan operation (tan x)