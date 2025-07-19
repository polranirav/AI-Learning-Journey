# Class variable vs instance variable

class Robot:
    category = "AI Machine"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

r1 = Robot("Alpha")
r2 = Robot("Beta")

print(r1.name, "-", r1.category)
print(r2.name, "-", r2.category)