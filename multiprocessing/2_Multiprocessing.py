# 2 Using multi processing Python

import time


# Create simple function that sleep in 1 second
def do_something():
    print('Sleeping 1 second ..')
    time.sleep(1)
    print('Done Sleeping')


if __name__ == '__main__':
    import multiprocessing

    start = time.perf_counter()

    # Create 2 multiprocessing and select function as target
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # Finish counting and show script runtime
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start,2)} second(s)")
