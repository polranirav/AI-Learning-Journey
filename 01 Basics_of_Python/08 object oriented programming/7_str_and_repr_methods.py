# Clean string representation of objects

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __repr__(self):
        return f"<Person name={self.name}>"

p = Person("Nirav")
print(str(p))     # Friendly
print(repr(p))    # Debugging/logging