# 1 Simple Syncronus Python


# Import Time and start counter
import time
start = time.perf_counter()


# Create simple function that sleep in 1 second
def do_something():
    print('Sleeping 1 second ..')
    time.sleep(1)
    print('Done Sleeping')


# Run the function twice, so expected run in 2s (@1 sec)
do_something()
do_something()


# Finish counting and show script runtime
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
