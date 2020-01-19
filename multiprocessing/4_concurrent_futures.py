# 4 Using concurrent future multiprocessing in python
import concurrent.futures
import time 

# Create simple function that sleep in 1 second
def do_something(seconds):
    print(f'Sleeping {seconds} second(s) ..')
    time.sleep(seconds)
    return 'Done Sleeping...'

if __name__ == '__main__':
    # Start counting
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        print(f1.result())
        print(f2.result())

    # Finish counting and show script runtime
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")
