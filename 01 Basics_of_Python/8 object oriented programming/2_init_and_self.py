# Using __init__ constructor and self keyword

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", "Labrador")
my_dog.bark()