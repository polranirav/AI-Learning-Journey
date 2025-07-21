# Generator that yields even numbers up to a limit

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i  # pause and resume, doesn't return all at once

for num in even_generator(10):
    print(num)
