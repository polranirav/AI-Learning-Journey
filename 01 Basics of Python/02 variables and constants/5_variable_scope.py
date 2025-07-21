# Demonstrating variable scope: local vs global

global_var = "I'm global"

def print_scope():
    local_var = "I'm local"
    print(global_var)  # Can access global variable
    print(local_var)   # Local variable

print_scope()

# print(local_var)  # ❌ Error: local_var is not defined outside function

# Modifying global variable inside function
def change_global():
    global global_var
    global_var = "Changed globally"

change_global()
print(global_var)  # "Changed globally"