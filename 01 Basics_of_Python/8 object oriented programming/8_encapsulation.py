# Encapsulation: hide internals using _ and __

class BankAccount:
    def __init__(self):
        self._balance = 0  # protected
        self.__pin = "1234"  # private

    def get_balance(self):
        return self._balance

    def __show_pin(self):
        print("PIN:", self.__pin)

account = BankAccount()
print("Balance:", account.get_balance())

# print(account.__pin)          ❌ Will raise AttributeError
# account.__show_pin()          ❌ Also inaccessible


# It refers to class as collections of data (variables) and methods that operate on that data.
# Public :-  self.var
# Protected :-  self._var
# Private :- self.__var


class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self._automation = 'automation programming'
        self.__selfdriving = 'selfdriving'

    def display(self):
        print(f"Car: {self.brand} {self.model} {self._automation}")
        print(f"Car: {self.__selfdriving}")
    # Creating an object
class Tata(Car):
        def display(self):
            print("Tata")

car = Car("Toyota", "Corolla")

# Accessing public members
print(car.brand)
print(car.model)
# print(car.__selfdriving)
car.display()

car1 = Tata("tata","safari")
car1.display()
print(car1._automation)
# Calling public

