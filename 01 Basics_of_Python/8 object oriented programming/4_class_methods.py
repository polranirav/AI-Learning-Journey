# Adding custom methods to class

class Calculator:
    def __init__(self, value):
        self.value = value

    def double(self):
        return self.value * 2

    def square(self):
        return self.value ** 2

c = Calculator(5)
print("Double:", c.double())
print("Square:", c.square())