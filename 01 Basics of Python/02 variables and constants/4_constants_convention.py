# Python doesn't have true constants, but we use naming conventions

PI = 3.14159
GRAVITY = 9.8

print("PI:", PI)
print("Gravity:", GRAVITY)

# Constants can still be changed, but shouldn't
PI = 3.14  # ❌ Not recommended
print("Modified PI:", PI)