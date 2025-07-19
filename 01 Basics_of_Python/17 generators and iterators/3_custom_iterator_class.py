# Custom iterator using __iter__ and __next__

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

cd = Countdown(3)
for i in cd:
    print("Countdown:", i)