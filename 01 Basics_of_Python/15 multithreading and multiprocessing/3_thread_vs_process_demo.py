import threading
import multiprocessing
import time

def run_task():
    for _ in range(3):
        time.sleep(1)

# Timing thread
start = time.time()
threads = [threading.Thread(target=run_task) for _ in range(3)]
for t in threads: t.start()
for t in threads: t.join()
print("Thread time:", round(time.time() - start, 2), "seconds")

# Timing process
start = time.time()
procs = [multiprocessing.Process(target=run_task) for _ in range(3)]
for p in procs: p.start()
for p in procs: p.join()
print("Process time:", round(time.time() - start, 2), "seconds")