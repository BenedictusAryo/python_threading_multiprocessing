# 2 Using threading in python

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


# Create threading, start and join
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

# Finish counting and show script runtime
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
