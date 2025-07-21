# Local vs global variable

x = "global"

def print_scope():
    x = "local"
    print("Inside function:", x)

print_scope()
print("Outside function:", x)