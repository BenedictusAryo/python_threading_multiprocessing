# 5 Using concurrent future threading in python

# Import Threading & Time
import concurrent.futures
import time

# Start counting
start = time.perf_counter()


# Create simple function that sleep in 'seconds' time
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)..')
    time.sleep(seconds)
    return 'Done Sleeping..'


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())


# Finish counting and show script runtime
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
