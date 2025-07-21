# Function that accepts any number of positional arguments

def sum_all(*args):
    print("Arguments passed:", args)

    for i in args:
        print("Double of", i, "is", i * 2)

    return sum(args)


print("Total sum:", sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))