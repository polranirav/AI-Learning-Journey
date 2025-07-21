from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(square, numbers))

    print("Squares:", results)