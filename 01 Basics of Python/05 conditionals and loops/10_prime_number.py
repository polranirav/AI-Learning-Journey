# Check if a number is prime

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is a prime number")
else:
    print("Enter a number greater than 1")