# Full structure of try-except flow

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Must be a number.")
else:
    print("You entered:", number)
finally:
    print("Execution complete.")