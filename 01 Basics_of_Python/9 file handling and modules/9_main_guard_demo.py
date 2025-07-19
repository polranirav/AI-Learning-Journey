# Code that only runs when file is run directly

def say_hello():
    print("Hello from main guard!")

if __name__ == "__main__":
    say_hello()