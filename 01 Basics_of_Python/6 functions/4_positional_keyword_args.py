# Positional vs keyword arguments

def user_info(name, age):
    print(f"Name: {name}, Age: {age}")

user_info("Nirav", 24)                 # positional
user_info(age=24, name="Nirav")       # keyword