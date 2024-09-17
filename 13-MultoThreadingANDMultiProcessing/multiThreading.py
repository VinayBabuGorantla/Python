'''
Multithreading
When to use Multi Threading
I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.
'''
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")

def print_letters():
    for i in "VinayBabuGorantla":
        time.sleep(2)
        print(f"Letter : {i}")

# Create 2 Threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t=time.time()

# Start Thread
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)