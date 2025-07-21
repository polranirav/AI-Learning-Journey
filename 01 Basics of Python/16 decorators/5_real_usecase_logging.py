def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Done with function: {func.__name__}")
        return result
    return wrapper

@log_call
def train_model():
    print("Training ML model...")

train_model()