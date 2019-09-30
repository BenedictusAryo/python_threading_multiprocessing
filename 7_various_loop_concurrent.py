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
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    result = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(result):
        print(f.result())


# Finish counting and show script runtime
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
