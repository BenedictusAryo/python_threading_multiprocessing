# 3 Using argument in multi processing Python
import time
import multiprocessing

# Create simple function that sleep in 1 second
def do_something(seconds):
    print(f'Sleeping {seconds} second(s) ..')
    time.sleep(1)
    print('Done Sleeping')
    

if __name__ == '__main__':

    start = time.perf_counter()

    # Create 2 multiprocessing and select function as target
    p1 = multiprocessing.Process(target=do_something, args=[2])
    p2 = multiprocessing.Process(target=do_something, args=[2])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # Finish counting and show script runtime
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")
