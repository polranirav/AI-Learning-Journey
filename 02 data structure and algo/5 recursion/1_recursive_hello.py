# Simple recursion demo

def say_hello(n):
    if n == 0:
        return
    print("Hello", n)
    say_hello(n - 1)

say_hello(8)

# Output:
# Hello 3
# Hello 2
# Hello 1