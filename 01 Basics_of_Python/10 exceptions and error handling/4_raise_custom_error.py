# Raise an error manually

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance!")
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except ValueError as e:
    print("Error:", e)