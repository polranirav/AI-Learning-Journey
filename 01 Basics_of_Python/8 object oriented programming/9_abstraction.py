# hiding unnecessary details
# Abstraction is one of the core principles of object-oriented programming (OOP) in Python.
# This way developers hide unnecessary implementation details and expose only the relevant functionalities.

# (1) Abstract classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("it is something special you don't understand.")

    @abstractmethod
    def stop(self):
        print("it is something more special you don't understand.")

    @abstractmethod
    def carzy(self):
        print("it is something more special you don't understand.")

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key ignition.")

    def stop(self):
        print("Car is stopping using the brake.")

car1 = Car()
car1.start()
car1.stop()
car1.carzy()


class Employee:
    __count = 0
    def __init__(self):
        Employee.__count += 1

    def employee_count(self):
        print("the number of employees is", Employee.__count)

emp = Employee()
emp1 = Employee()
emp2 = Employee()
emp3 = Employee()
emp.employee_count()

# print(emp.__count) ///  'Employee' object has no attribute '__count'

