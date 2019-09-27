# 3 Using for loop threading in python

# Import Threading & Time
import threading
import time

# Start counting
start = time.perf_counter()


# Create simple function that sleep in 1 second
def do_something():
    print('Sleeping 1 second..')
    time.sleep(1)
    print('Done Sleeping..')


# Create empty list
threads = []

# Create for loop threading to repeat 10 times
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)


# Then join each thread in Threads list
for thread in threads:
    thread.join()


# Finish counting and show script runtime
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
