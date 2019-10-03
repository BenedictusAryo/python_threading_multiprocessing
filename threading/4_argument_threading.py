# 4 Using function arguments threading in python

# Import Threading & Time
import threading
import time

# Start counting
start = time.perf_counter()


# Create simple function that sleep in 'seconds' time
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)..')
    time.sleep(seconds)
    print('Done Sleeping..')


# Create empty list
threads = []

# Create for loop threading to repeat 10 times
for _ in range(10):
    t = threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)


# Then join each thread in Threads list
for thread in threads:
    thread.join()


# Finish counting and show script runtime
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
