# Recursive Fibonacci (inefficient but classic)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(7):
    print(f"fib({i}) =", fib(i))