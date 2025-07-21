import threading

def task():
    print("Running:", threading.current_thread().name)

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
t1.join()
t2.join()