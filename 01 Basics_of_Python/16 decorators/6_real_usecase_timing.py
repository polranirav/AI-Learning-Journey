import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {round(end - start, 4)}s")
        return result
    return wrapper

@timer
def compute():
    time.sleep(1)
    print("Computation complete.")

compute()