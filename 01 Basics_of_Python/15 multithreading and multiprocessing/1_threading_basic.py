import threading

def print_numbers():
    for i in range(5):
        print("Thread:", i)

# Create and start thread
t1 = threading.Thread(target=print_numbers)
t1.start()
t1.join()  # Wait for thread to finish

print("Main thread finished.")