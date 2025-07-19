import multiprocessing

def calc_square(n):
    total = 0
    for i in range(n):
        total += i * i
    print("Sum of squares:", total)

# Heavy computation
if __name__ == '__main__':
    numbers = [10_000_000, 12_000_000, 14_000_000]
    processes = [multiprocessing.Process(target=calc_square, args=(num,)) for num in numbers]

    for p in processes: p.start()
    for p in processes: p.join()

    print("All CPU-bound tasks completed.")