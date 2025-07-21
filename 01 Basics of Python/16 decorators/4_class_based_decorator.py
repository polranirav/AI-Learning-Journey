class LogCalls:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)

@LogCalls
def multiply(a, b):
    return a * b

print(multiply(2, 4))