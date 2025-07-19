import multiprocessing

def show_process():
    for i in range(5):
        print("Process:", i)

# Create and run process
p1 = multiprocessing.Process(target=show_process)
p1.start()
p1.join()

print("Main process finished.")