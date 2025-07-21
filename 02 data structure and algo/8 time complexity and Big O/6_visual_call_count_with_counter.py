# Count how many times a function is called (to visualize O growth)

counter = 0

def call_me(n):
    global counter
    if n == 0:
        return
    counter += 1
    call_me(n - 1)  # Recursive O(n)

call_me(10)
print("Function called:", counter, "times")  # Shows recursion depth