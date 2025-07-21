# Trace call stack for debug

def trace(n):
    print("Entering:", n)
    if n == 0:
        print("Base case hit")
        return
    trace(n - 1)
    print("Returning from:", n)

trace(3)

# Shows how recursion stack unwinds