# Demonstrates dynamic typing: variable type can change at runtime

x = 10
print("x is", x, "| Type:", type(x))

x = "AI Engineer"
print("Now x is", x, "| Type:", type(x))

# 🔸 Function used here — just for demo.
# We'll learn functions properly in Folder 6: Functions.
def greet(name: str) -> str:
    return "Hello, " + name

print(greet("Nirav"))