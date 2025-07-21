# Compare named function vs lambda

def square_fn(x):
    return x * x

square_lambda = lambda x: x * x

print("Function result:", square_fn(5))
print("Lambda result:", square_lambda(5))