# Check if brackets are balanced using stack

def is_balanced(expr):
    stack = []
    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack: return False
            if (stack[-1], ch) not in [("(", ")"), ("[", "]"), ("{", "}")]:
                return False
            stack.pop()
    return not stack

print(is_balanced("({[()]})"))  # ✅ True
print(is_balanced("((]"))       # ❌ False